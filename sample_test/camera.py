import cv2
import mediapipe as mp
import pygame
import threading

# Initialize MediaPipe
mp_pose = mp.solutions.pose
pose = mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5)

# Pygame setup
pygame.init()
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Hip-Controlled Brick")

clock = pygame.time.Clock()

# Brick properties
brick_width = 100
brick_height = 30
brick_x = screen_width // 2
brick_y = screen_height - 60
brick_color = (255, 100, 100)

# Shared data between threads
hip_x = screen_width // 2
running = True

# Webcam tracking function
def track_hip():
    global hip_x, running
    cap = cv2.VideoCapture(0)

    while running:
        ret, frame = cap.read()
        if not ret:
            break

        h, w, _ = frame.shape
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = pose.process(image)

        if results.pose_landmarks:
            landmarks = results.pose_landmarks.landmark
            left_hip = landmarks[mp_pose.PoseLandmark.LEFT_HIP]
            right_hip = landmarks[mp_pose.PoseLandmark.RIGHT_HIP]

            # Average X position of hips
            avg_hip_x = (left_hip.x + right_hip.x) / 2.0
            hip_x = int(avg_hip_x * screen_width)  # Scale to screen

        if cv2.waitKey(1) & 0xFF == ord('q'):
            running = False
            break

    cap.release()

# Start tracking in a separate thread
tracking_thread = threading.Thread(target=track_hip)
tracking_thread.start()

# Game loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((30, 30, 30))

    # Move brick towards hip position
    brick_x += (hip_x - (brick_x + brick_width // 2)) * 0.2  # Smooth movement

    pygame.draw.rect(screen, brick_color, (brick_x, brick_y, brick_width, brick_height))
    pygame.display.flip()
    clock.tick(60)

# Cleanup
pygame.quit()
running = False
tracking_thread.join()
