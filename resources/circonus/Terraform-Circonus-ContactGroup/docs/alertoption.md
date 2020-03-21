# Terraform::Circonus::ContactGroup AlertOption

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#escalateafter" title="EscalateAfter">EscalateAfter</a>" : <i>String</i>,
    "<a href="#escalateto" title="EscalateTo">EscalateTo</a>" : <i>String</i>,
    "<a href="#reminder" title="Reminder">Reminder</a>" : <i>String</i>,
    "<a href="#severity" title="Severity">Severity</a>" : <i>Double</i>
}
</pre>

### YAML

<pre>
<a href="#escalateafter" title="EscalateAfter">EscalateAfter</a>: <i>String</i>
<a href="#escalateto" title="EscalateTo">EscalateTo</a>: <i>String</i>
<a href="#reminder" title="Reminder">Reminder</a>: <i>String</i>
<a href="#severity" title="Severity">Severity</a>: <i>Double</i>
</pre>

## Properties

#### EscalateAfter

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EscalateTo

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Reminder

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Severity

_Required_: Yes
_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

