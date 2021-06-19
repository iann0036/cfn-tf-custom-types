# TF::AWS::GlueTrigger ActionsDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#arguments" title="Arguments">Arguments</a>" : <i>[ <a href="argumentsdefinition.md">ArgumentsDefinition</a>, ... ]</i>,
    "<a href="#crawlername" title="CrawlerName">CrawlerName</a>" : <i>String</i>,
    "<a href="#jobname" title="JobName">JobName</a>" : <i>String</i>,
    "<a href="#securityconfiguration" title="SecurityConfiguration">SecurityConfiguration</a>" : <i>String</i>,
    "<a href="#timeout" title="Timeout">Timeout</a>" : <i>Double</i>,
    "<a href="#notificationproperty" title="NotificationProperty">NotificationProperty</a>" : <i>[ <a href="notificationpropertydefinition.md">NotificationPropertyDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#arguments" title="Arguments">Arguments</a>: <i>
      - <a href="argumentsdefinition.md">ArgumentsDefinition</a></i>
<a href="#crawlername" title="CrawlerName">CrawlerName</a>: <i>String</i>
<a href="#jobname" title="JobName">JobName</a>: <i>String</i>
<a href="#securityconfiguration" title="SecurityConfiguration">SecurityConfiguration</a>: <i>String</i>
<a href="#timeout" title="Timeout">Timeout</a>: <i>Double</i>
<a href="#notificationproperty" title="NotificationProperty">NotificationProperty</a>: <i>
      - <a href="notificationpropertydefinition.md">NotificationPropertyDefinition</a></i>
</pre>

## Properties

#### Arguments

_Required_: No

_Type_: List of <a href="argumentsdefinition.md">ArgumentsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CrawlerName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### JobName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecurityConfiguration

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeout

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NotificationProperty

_Required_: No

_Type_: List of <a href="notificationpropertydefinition.md">NotificationPropertyDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

