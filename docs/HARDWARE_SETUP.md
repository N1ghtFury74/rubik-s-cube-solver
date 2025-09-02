# 🔧 Hardware Setup Guide

## Bill of Materials (900 EGP Total)

| Component | Quantity | Estimated Cost (EGP) | Purpose |
|-----------|----------|---------------------|---------|
| Arduino Uno/Nano | 1 | 150 | Main controller |
| Stepper Motors (28BYJ-48) | 6 | 300 | Face rotation motors |
| ULN2003 Driver Boards | 6 | 120 | Motor control |
| 12V Power Supply | 1 | 80 | Motor power |
| Jumper Wires | 1 set | 30 | Connections |
| Breadboard/PCB | 1 | 50 | Circuit assembly |
| 3D Printed Parts | 1 set | 100 | Cube holder mechanism |
| Miscellaneous | - | 70 | Screws, bearings, etc. |

## Wiring Diagram

```
Arduino Pins → Stepper Motors
┌─────────────────────────────────┐
│ Face | Step Pin | Dir Pin | Motor│
│------|----------|---------|------│
│  U   |    3     |    2    | Top  │
│  D   |    5     |    4    | Bottom│
│  L   |   11     |   10    | Left │
│  R   |   13     |   12    | Right│
│  F   |    7     |    6    | Front│
│  B   |    9     |    8    | Back │
└─────────────────────────────────┘
```

## Assembly Instructions

### 1. Motor Mounting
- Mount each stepper motor to control one face of the cube
- Ensure motors can rotate cube faces 90° and 180°
- Use gears or direct coupling for reliable torque transfer

### 2. Electronics Assembly
- Connect each motor to its ULN2003 driver board
- Wire driver boards to Arduino according to pin diagram
- Connect 12V power supply to motor drivers
- Use common ground for all components

### 3. Cube Holder Design
- Design holder to securely grip cube during solving
- Allow free rotation of each face
- Minimize friction and backlash
- Consider using bearings for smooth operation

### 4. Calibration
- Test each motor individually
- Verify 90° rotation accuracy
- Adjust step counts if needed (default: 50 steps = 90°)
- Fine-tune timing delays for optimal speed

## Safety Considerations

⚠️ **Important Safety Notes:**
- Always disconnect power when wiring
- Use appropriate fuses for motor power supply
- Ensure cube holder is secure to prevent cube ejection
- Test emergency stop functionality

## Troubleshooting

### Common Issues:
1. **Motor not moving**: Check wiring and power supply
2. **Inaccurate rotation**: Calibrate step counts
3. **Communication errors**: Verify COM port and baud rate
4. **Cube slipping**: Improve holder grip mechanism

### Performance Optimization:
- Reduce mechanical friction
- Optimize move delays in Arduino code
- Use quality stepper motors for consistency
- Implement acceleration/deceleration curves
