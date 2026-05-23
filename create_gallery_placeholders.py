import base64
from pathlib import Path
jpg_base64 = "/9j/4AAQSkZJRgABAQEASABIAAD/2wBDAP//////////////////////////////////////////////////////////////////////////////////////2wBDAf//////////////////////////////////////////////////////////////////////////////////////wAARCAABAAEDASIAAhEBAxEB/8QAFwAAAwEAAAAAAAAAAAAAAAAAAAUGB//EABwQAAICAwEAAAAAAAAAAAAAAAECAAMREhMxQf/EABQBAQAAAAAAAAAAAAAAAAAAAAD/xAAVEQEBAAAAAAAAAAAAAAAAAAABAP/aAAwDAQACEQMRAD8A+//Z"
img = base64.b64decode(jpg_base64)
names = [
    'service sunday.jpg',
    'youth camp.jpg',
    'community outreach.jpeg',
    'choir practice',
    'bible study',
]
for name in names:
    Path(name).write_bytes(img)
print('created', len(names), 'files')
