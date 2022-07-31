From continuumio/miniconda3:latest

WORKDIR /app

EXPOSE 5000

#Copy environment.yml
COPY environment.yml .

#Run
RUN conda env create -f environment.yml
RUN conda activate twtapp
RUN echo "checking....for..dependencies"
RUN python3 -c "import flask"

COPY app.py .
CMD ["python3", "app.py"]
