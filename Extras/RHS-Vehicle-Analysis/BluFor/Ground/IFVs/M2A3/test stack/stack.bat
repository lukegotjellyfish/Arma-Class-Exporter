ffmpeg -i a.gif -vf scale=-1:375 ahstack.gif
ffmpeg -i d.gif -vf scale=-1:375 dhstack.gif
ffmpeg -i e.gif -vf scale=-1:375 ehstack.gif

ffmpeg -i a.gif -vf scale=600:-1 avstack.gif
ffmpeg -i d.gif -vf scale=600:-1 dvstack.gif
ffmpeg -i e.gif -vf scale=600:-1 evstack.gif

ffmpeg -i ahstack.gif -i dhstack.gif -i ehstack.gif -filter_complex hstack=inputs=3 a-d-e-hstacked.gif
ffmpeg -i avstack.gif -i dvstack.gif -i evstack.gif -filter_complex vstack=inputs=3 a-d-e-vstacked.gif

PAUSE