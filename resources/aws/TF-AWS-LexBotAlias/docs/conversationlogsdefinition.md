# TF::AWS::LexBotAlias ConversationLogsDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#iamrolearn" title="IamRoleArn">IamRoleArn</a>" : <i>String</i>,
    "<a href="#logsettings" title="LogSettings">LogSettings</a>" : <i>[ <a href="logsettingsdefinition.md">LogSettingsDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#iamrolearn" title="IamRoleArn">IamRoleArn</a>: <i>String</i>
<a href="#logsettings" title="LogSettings">LogSettings</a>: <i>
      - <a href="logsettingsdefinition.md">LogSettingsDefinition</a></i>
</pre>

## Properties

#### IamRoleArn

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LogSettings

_Required_: No

_Type_: List of <a href="logsettingsdefinition.md">LogSettingsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

