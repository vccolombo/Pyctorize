import click
import os
from moviepy.editor import VideoFileClip


class Movie:
    def __init__(self, file_name, path_to_save, start_time, step):
        self.file_name = file_name
        self.path_to_save = path_to_save
        self.start_time = start_time
        self.step = step

    def extract_frames(self):
        clip = VideoFileClip(self.file_name)
        duration = clip.duration * 1000

        # TODO: Avoid user to input time bigger than clip duration

        # if self.step  is 0, only one frame must be taken
        if self.step == 0:
            time = self.start_time / 1000  # time in s
            imgpath = os.path.join(self.path_to_save, '{}.png'.format(time))
            clip.save_frame(imgpath, time)
            return

        # else must take a frame every self.step seconds
        times = [(t + self.start_time) / 1000 for t in range(self.start_time, int(duration), self.step)]
        for t in times:
            imgpath = os.path.join(self.path_to_save, '{}.png'.format(t))
            clip.save_frame(imgpath, t)


@click.command()
@click.argument('filename', type=click.Path(exists=True))
@click.option('--path', '-p', type=click.Path(exists=True, dir_okay=True), default='.')
@click.option('--start-time', '-t', default=0)
@click.option('--step', '-s', default=0)
def pyctorize(filename, path, start_time, step):
    movie = Movie(filename, path, start_time, step)
    click.echo("Generating images...")
    movie.extract_frames()


if __name__ == '__main__':
    pyctorize()
