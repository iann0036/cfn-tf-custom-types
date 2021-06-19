# TF::SignalFx::OrgToken

Manage SignalFx org tokens.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::SignalFx::OrgToken",
    "Properties" : {
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#disabled" title="Disabled">Disabled</a>" : <i>Boolean</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#notifications" title="Notifications">Notifications</a>" : <i>[ String, ... ]</i>,
        "<a href="#dpmlimits" title="DpmLimits">DpmLimits</a>" : <i>[ <a href="dpmlimitsdefinition.md">DpmLimitsDefinition</a>, ... ]</i>,
        "<a href="#hostorusagelimits" title="HostOrUsageLimits">HostOrUsageLimits</a>" : <i>[ <a href="hostorusagelimitsdefinition.md">HostOrUsageLimitsDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::SignalFx::OrgToken
Properties:
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#disabled" title="Disabled">Disabled</a>: <i>Boolean</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#notifications" title="Notifications">Notifications</a>: <i>
      - String</i>
    <a href="#dpmlimits" title="DpmLimits">DpmLimits</a>: <i>
      - <a href="dpmlimitsdefinition.md">DpmLimitsDefinition</a></i>
    <a href="#hostorusagelimits" title="HostOrUsageLimits">HostOrUsageLimits</a>: <i>
      - <a href="hostorusagelimitsdefinition.md">HostOrUsageLimitsDefinition</a></i>
</pre>

## Properties

#### Description

Description of the token.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Disabled

Flag that controls enabling the token. If set to `true`, the token is disabled, and you can't use it for authentication. Defaults to `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Name of the token.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Notifications

Where to send notifications about this token's limits. Please consult the [Notification Format](https://www.terraform.io/docs/providers/signalfx/r/detector.html#notification-format) laid out in detectors.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DpmLimits

_Required_: No

_Type_: List of <a href="dpmlimitsdefinition.md">DpmLimitsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HostOrUsageLimits

_Required_: No

_Type_: List of <a href="hostorusagelimitsdefinition.md">HostOrUsageLimitsDefinition</a>

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

#### Secret

The secret token created by the API. You cannot set this value.

