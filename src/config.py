CONFIG_PATH="res/config.sh"
CREDENTIAL_VAR="SERVICE_ACCOUNT_KEY"
DEFAULT_CREDENTIALS_PATH="res/credentials.json"


TRUE : int = ~0
FALSE : int = 0

DELETE_ON_FORMAT       = 0b1       & FALSE
DELETE_ON_VALUE        = 0b10      & FALSE
DELETE_ON_DATE_PATTERN = 0b100     & FALSE
DELETE_ON_LIFETIME     = 0b1000    & TRUE
DELETE_ON_GLOB         = 0b10000   & TRUE
DELETE_ON_REGEX        = 0b100000  & TRUE

