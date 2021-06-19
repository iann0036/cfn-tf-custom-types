# TF::Volterra::AlertPolicy RoutesDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#alertname" title="Alertname">Alertname</a>" : <i>String</i>,
    "<a href="#alertnameregex" title="AlertnameRegex">AlertnameRegex</a>" : <i>String</i>,
    "<a href="#any" title="Any">Any</a>" : <i>Boolean</i>,
    "<a href="#dontsend" title="DontSend">DontSend</a>" : <i>Boolean</i>,
    "<a href="#send" title="Send">Send</a>" : <i>Boolean</i>,
    "<a href="#custom" title="Custom">Custom</a>" : <i>[ <a href="customdefinition.md">CustomDefinition</a>, ... ]</i>,
    "<a href="#group" title="Group">Group</a>" : <i>[ <a href="groupdefinition.md">GroupDefinition</a>, ... ]</i>,
    "<a href="#notificationparameters" title="NotificationParameters">NotificationParameters</a>" : <i>[ <a href="notificationparametersdefinition.md">NotificationParametersDefinition</a>, ... ]</i>,
    "<a href="#severity" title="Severity">Severity</a>" : <i>[ <a href="severitydefinition.md">SeverityDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#alertname" title="Alertname">Alertname</a>: <i>String</i>
<a href="#alertnameregex" title="AlertnameRegex">AlertnameRegex</a>: <i>String</i>
<a href="#any" title="Any">Any</a>: <i>Boolean</i>
<a href="#dontsend" title="DontSend">DontSend</a>: <i>Boolean</i>
<a href="#send" title="Send">Send</a>: <i>Boolean</i>
<a href="#custom" title="Custom">Custom</a>: <i>
      - <a href="customdefinition.md">CustomDefinition</a></i>
<a href="#group" title="Group">Group</a>: <i>
      - <a href="groupdefinition.md">GroupDefinition</a></i>
<a href="#notificationparameters" title="NotificationParameters">NotificationParameters</a>: <i>
      - <a href="notificationparametersdefinition.md">NotificationParametersDefinition</a></i>
<a href="#severity" title="Severity">Severity</a>: <i>
      - <a href="severitydefinition.md">SeverityDefinition</a></i>
</pre>

## Properties

#### Alertname

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AlertnameRegex

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Any

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DontSend

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Send

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Custom

_Required_: No

_Type_: List of <a href="customdefinition.md">CustomDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Group

_Required_: No

_Type_: List of <a href="groupdefinition.md">GroupDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NotificationParameters

_Required_: No

_Type_: List of <a href="notificationparametersdefinition.md">NotificationParametersDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Severity

_Required_: No

_Type_: List of <a href="severitydefinition.md">SeverityDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

