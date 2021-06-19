# TF::Volterra::CloudCredentials ClientSecretDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#secretencodingtype" title="SecretEncodingType">SecretEncodingType</a>" : <i>String</i>,
    "<a href="#blindfoldsecretinfo" title="BlindfoldSecretInfo">BlindfoldSecretInfo</a>" : <i>[ <a href="blindfoldsecretinfodefinition.md">BlindfoldSecretInfoDefinition</a>, ... ]</i>,
    "<a href="#blindfoldsecretinfointernal" title="BlindfoldSecretInfoInternal">BlindfoldSecretInfoInternal</a>" : <i>[ <a href="blindfoldsecretinfointernaldefinition.md">BlindfoldSecretInfoInternalDefinition</a>, ... ]</i>,
    "<a href="#clearsecretinfo" title="ClearSecretInfo">ClearSecretInfo</a>" : <i>[ <a href="clearsecretinfodefinition.md">ClearSecretInfoDefinition</a>, ... ]</i>,
    "<a href="#vaultsecretinfo" title="VaultSecretInfo">VaultSecretInfo</a>" : <i>[ <a href="vaultsecretinfodefinition.md">VaultSecretInfoDefinition</a>, ... ]</i>,
    "<a href="#wingmansecretinfo" title="WingmanSecretInfo">WingmanSecretInfo</a>" : <i>[ <a href="wingmansecretinfodefinition.md">WingmanSecretInfoDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#secretencodingtype" title="SecretEncodingType">SecretEncodingType</a>: <i>String</i>
<a href="#blindfoldsecretinfo" title="BlindfoldSecretInfo">BlindfoldSecretInfo</a>: <i>
      - <a href="blindfoldsecretinfodefinition.md">BlindfoldSecretInfoDefinition</a></i>
<a href="#blindfoldsecretinfointernal" title="BlindfoldSecretInfoInternal">BlindfoldSecretInfoInternal</a>: <i>
      - <a href="blindfoldsecretinfointernaldefinition.md">BlindfoldSecretInfoInternalDefinition</a></i>
<a href="#clearsecretinfo" title="ClearSecretInfo">ClearSecretInfo</a>: <i>
      - <a href="clearsecretinfodefinition.md">ClearSecretInfoDefinition</a></i>
<a href="#vaultsecretinfo" title="VaultSecretInfo">VaultSecretInfo</a>: <i>
      - <a href="vaultsecretinfodefinition.md">VaultSecretInfoDefinition</a></i>
<a href="#wingmansecretinfo" title="WingmanSecretInfo">WingmanSecretInfo</a>: <i>
      - <a href="wingmansecretinfodefinition.md">WingmanSecretInfoDefinition</a></i>
</pre>

## Properties

#### SecretEncodingType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BlindfoldSecretInfo

_Required_: No

_Type_: List of <a href="blindfoldsecretinfodefinition.md">BlindfoldSecretInfoDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BlindfoldSecretInfoInternal

_Required_: No

_Type_: List of <a href="blindfoldsecretinfointernaldefinition.md">BlindfoldSecretInfoInternalDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClearSecretInfo

_Required_: No

_Type_: List of <a href="clearsecretinfodefinition.md">ClearSecretInfoDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VaultSecretInfo

_Required_: No

_Type_: List of <a href="vaultsecretinfodefinition.md">VaultSecretInfoDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WingmanSecretInfo

_Required_: No

_Type_: List of <a href="wingmansecretinfodefinition.md">WingmanSecretInfoDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

