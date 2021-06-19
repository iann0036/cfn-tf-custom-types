# TF::Circonus::Maintenance

The ``circonus_maintenance`` resource creates and manages a
single [maintenance window resource](https://login.circonus.com/resources/docs/user/Alerting/Maintenance.html)
which can reference a check, ruleset, target or entire account.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Circonus::Maintenance",
    "Properties" : {
        "<a href="#account" title="Account">Account</a>" : <i>String</i>,
        "<a href="#check" title="Check">Check</a>" : <i>String</i>,
        "<a href="#notes" title="Notes">Notes</a>" : <i>String</i>,
        "<a href="#ruleset" title="RuleSet">RuleSet</a>" : <i>String</i>,
        "<a href="#severities" title="Severities">Severities</a>" : <i>[ String, ... ]</i>,
        "<a href="#start" title="Start">Start</a>" : <i>String</i>,
        "<a href="#stop" title="Stop">Stop</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ String, ... ]</i>,
        "<a href="#target" title="Target">Target</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Circonus::Maintenance
Properties:
    <a href="#account" title="Account">Account</a>: <i>String</i>
    <a href="#check" title="Check">Check</a>: <i>String</i>
    <a href="#notes" title="Notes">Notes</a>: <i>String</i>
    <a href="#ruleset" title="RuleSet">RuleSet</a>: <i>String</i>
    <a href="#severities" title="Severities">Severities</a>: <i>
      - String</i>
    <a href="#start" title="Start">Start</a>: <i>String</i>
    <a href="#stop" title="Stop">Stop</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - String</i>
    <a href="#target" title="Target">Target</a>: <i>String</i>
</pre>

## Properties

#### Account

A string referencing the account CID to have maintenance on, mutually exclusive
with `check`, `rule_set`, and `target`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Check

A string referencing the check CID to have maintenance on, mutually exclusive
with `account`, `rule_set`, and `target`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Notes

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RuleSet

A string referencing the rule_set CID to have maintenance on, mutually exclusive
with `account`, `check`, and `target`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Severities

A list of strings determining which severities to put into maintenance.
Must be in the range: "1"-"5".

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Start

An RFC3339 timestamp string which indicates the start of the maintenance window.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Stop

An RFC3339 timestamp string which indicates the end of the maintenance window.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

A list of tags assigned to the maintenance window.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Target

A string referencing the check target (host) to have maintenance on, mutually exclusive
with `account`, `rule_set`, and `check`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Id

Returns the <code>Id</code> value.

