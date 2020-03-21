# Terraform::AzureRM::BackupPolicyVm Backup

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#frequency" title="Frequency">Frequency</a>" : <i>String</i>,
    "<a href="#time" title="Time">Time</a>" : <i>String</i>,
    "<a href="#weekdays" title="Weekdays">Weekdays</a>" : <i>[ String, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#frequency" title="Frequency">Frequency</a>: <i>String</i>
<a href="#time" title="Time">Time</a>: <i>String</i>
<a href="#weekdays" title="Weekdays">Weekdays</a>: <i>
      - String</i>
</pre>

## Properties

#### Frequency

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Time

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Weekdays

_Required_: No
_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

