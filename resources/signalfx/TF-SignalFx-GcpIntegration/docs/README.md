# TF::SignalFx::GcpIntegration

SignalFx GCP Integration

~> **NOTE** When managing integrations you'll need to use an admin token to authenticate the SignalFx provider. Otherwise you'll receive a 4xx error.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::SignalFx::GcpIntegration",
    "Properties" : {
        "<a href="#enabled" title="Enabled">Enabled</a>" : <i>Boolean</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#namedtoken" title="NamedToken">NamedToken</a>" : <i>String</i>,
        "<a href="#pollrate" title="PollRate">PollRate</a>" : <i>Double</i>,
        "<a href="#services" title="Services">Services</a>" : <i>[ String, ... ]</i>,
        "<a href="#whitelist" title="Whitelist">Whitelist</a>" : <i>[ String, ... ]</i>,
        "<a href="#projectservicekeys" title="ProjectServiceKeys">ProjectServiceKeys</a>" : <i>[ <a href="projectservicekeysdefinition.md">ProjectServiceKeysDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::SignalFx::GcpIntegration
Properties:
    <a href="#enabled" title="Enabled">Enabled</a>: <i>Boolean</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#namedtoken" title="NamedToken">NamedToken</a>: <i>String</i>
    <a href="#pollrate" title="PollRate">PollRate</a>: <i>Double</i>
    <a href="#services" title="Services">Services</a>: <i>
      - String</i>
    <a href="#whitelist" title="Whitelist">Whitelist</a>: <i>
      - String</i>
    <a href="#projectservicekeys" title="ProjectServiceKeys">ProjectServiceKeys</a>: <i>
      - <a href="projectservicekeysdefinition.md">ProjectServiceKeysDefinition</a></i>
</pre>

## Properties

#### Enabled

Whether the integration is enabled.

_Required_: Yes

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Name of the integration.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NamedToken

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PollRate

GCP integration poll rate in seconds. Can be set to either 60 or 300 (1 minute or 5 minutes).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Services

GCP service metrics to import. Can be an empty list, or not included, to import 'All services'. See the documentation for [Creating Integrations](https://developers.signalfx.com/integrations_reference.html#operation/Create%20Integration) for valid values.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Whitelist

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProjectServiceKeys

_Required_: No

_Type_: List of <a href="projectservicekeysdefinition.md">ProjectServiceKeysDefinition</a>

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

