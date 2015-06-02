# hedwig

Hedwig will deliver gifs to your Slack channel.


## Usage

Gifs in every slack channel can be distracting. So, you will have to create a special channel **#hedwig**. From any Slack channel, just type `/hedwig [gif_keyword]`. The gif will show up in **#hedwig** channel.

## Integrate with your team

1. Go to your channel
2. Click on **Configure Integrations**.
3. Scroll all the way down to **DIY Integrations & Customizations section**.
4. Click on **Add** next to **Slash Commands**.
  - Command: `/hedwig`
  - URL: `http://hedwiglovesslack.herokuapp.com/hedwig`
  - Method: `POST`
  - For the **Autocomplete help text**, check to show the command in autocomplete list.
    - Description: `Hedwig will deliver gifs to your Slack channel. `
    - Usage hint: `[gif_keyword]`
  - Descriptive Label: `Search for gifs`

## Developing

```python
# Install python dependencies
$ pip install -r requirements.txt

# Start the server
$ python app.py
```
