def XYCirconference(center, radius, angle):
    global xcenter
    rad = math.radians(angle)
    xcenter = center[0]; ycenter = center[1]
    x = xcenter + radius * math.cos(rad)
    y = ycenter + radius * math.sin(rad)
    return [x,y]
