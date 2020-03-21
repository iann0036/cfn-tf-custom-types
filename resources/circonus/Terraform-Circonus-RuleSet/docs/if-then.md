# Terraform::Circonus::RuleSet If Then

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#after" title="After">After</a>" : <i>String</i>,
    "<a href="#notify" title="Notify">Notify</a>" : <i>[ String, ... ]</i>,
    "<a href="#severity" title="Severity">Severity</a>" : <i>Double</i>
}
</pre>

### YAML

<pre>
<a href="#after" title="After">After</a>: <i>String</i>
<a href="#notify" title="Notify">Notify</a>: <i>
      - String</i>
<a href="#severity" title="Severity">Severity</a>: <i>Double</i>
</pre>

## Properties

#### After

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Notify

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Severity

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

