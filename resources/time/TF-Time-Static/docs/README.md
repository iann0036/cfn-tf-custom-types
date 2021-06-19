# TF::Time::Static

Manages a static time resource, which keeps a locally sourced UTC timestamp stored in the Terraform state. This prevents perpetual differences caused by using the [`timestamp()` function](https://www.terraform.io/docs/configuration/functions/timestamp.html).

-> Further manipulation of incoming or outgoing values can be accomplished with the [`formatdate()` function](https://www.terraform.io/docs/configuration/functions/formatdate.html) and the [`timeadd()` function](https://www.terraform.io/docs/configuration/functions/timeadd.html).

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Time::Static",
    "Properties" : {
        "<a href="#rfc3339" title="Rfc3339">Rfc3339</a>" : <i>String</i>,
        "<a href="#triggers" title="Triggers">Triggers</a>" : <i>[ <a href="triggersdefinition.md">TriggersDefinition</a>, ... ]</i>,
    }
}
</pre>

### YAML

<pre>
Type: TF::Time::Static
Properties:
    <a href="#rfc3339" title="Rfc3339">Rfc3339</a>: <i>String</i>
    <a href="#triggers" title="Triggers">Triggers</a>: <i>
      - <a href="triggersdefinition.md">TriggersDefinition</a></i>
</pre>

## Properties

#### Rfc3339

Configure the base timestamp with an UTC [RFC3339 time string](https://tools.ietf.org/html/rfc3339#section-5.8) (`YYYY-MM-DDTHH:MM:SSZ`). Defaults to the current time.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Triggers

Arbitrary map of values that, when changed, will trigger a new base timestamp value to be saved. See [the main provider documentation](../index.html) for more information.

_Required_: No

_Type_: List of <a href="triggersdefinition.md">TriggersDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Day

Returns the <code>Day</code> value.

#### Hour

Returns the <code>Hour</code> value.

#### Id

Returns the <code>Id</code> value.

#### Minute

Returns the <code>Minute</code> value.

#### Month

Returns the <code>Month</code> value.

#### Second

Returns the <code>Second</code> value.

#### Unix

Returns the <code>Unix</code> value.

#### Year

Returns the <code>Year</code> value.

