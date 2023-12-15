import logging
import hydra
from omegaconf import DictConfig

LOG_FORMAT = "%(asctime)s %(message)s"
logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)

action_choices = ["action1", "action2"]


@hydra.main(version_base=None, config_path="config", config_name="config")
def main(cfg: DictConfig) -> None:
    from src import app

    app.run(cfg["action"], cfg["param1"])


if __name__ == "__main__":
    main()
