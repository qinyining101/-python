# 安装依赖：pip install opencv-contrib-python
import cv2
import tkinter.messagebox as tk

tracker = cv2.TrackerCSRT_create()
tracking = 0
cap = cv2.VideoCapture(0)
tk.showinfo('提示', '按1键开始选择区域追踪\n按Esc键退出')

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # 检查按键1开启追踪
    if cv2.waitKey(1) == ord('1'):
        tracking = 1
        tk.showinfo('提示', '按空格/回车键结束选择区域追踪')
        roi = cv2.selectROI('Tracking_target_window', frame, 0)
        tracker.init(frame, roi)
        
        # 显式关闭ROI选择窗口
        cv2.destroyWindow('Tracking_target_window')

    # 进行追踪
    if tracking:
        success, box = tracker.update(frame)
        if success:
            x, y, w, h = [int(v) for v in box]  # 确保坐标为整数
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # 显示图像
    cv2.imshow('tracking', frame)

    # 检查Esc键退出
    if cv2.waitKey(1) == 27:  # 27 是 ESC 的 ASCII 值
        break

cap.release()
cv2.destroyAllWindows()
