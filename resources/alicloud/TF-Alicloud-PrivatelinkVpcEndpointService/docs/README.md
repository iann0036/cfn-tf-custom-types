# TF::Alicloud::PrivatelinkVpcEndpointService

CloudFormation equivalent of alicloud_privatelink_vpc_endpoint_service

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Alicloud::PrivatelinkVpcEndpointService",
    "Properties" : {
        "<a href="#autoacceptconnection" title="AutoAcceptConnection">AutoAcceptConnection</a>" : <i>Boolean</i>,
        "<a href="#connectbandwidth" title="ConnectBandwidth">ConnectBandwidth</a>" : <i>Double</i>,
        "<a href="#dryrun" title="DryRun">DryRun</a>" : <i>Boolean</i>,
        "<a href="#payer" title="Payer">Payer</a>" : <i>String</i>,
        "<a href="#servicedescription" title="ServiceDescription">ServiceDescription</a>" : <i>String</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Alicloud::PrivatelinkVpcEndpointService
Properties:
    <a href="#autoacceptconnection" title="AutoAcceptConnection">AutoAcceptConnection</a>: <i>Boolean</i>
    <a href="#connectbandwidth" title="ConnectBandwidth">ConnectBandwidth</a>: <i>Double</i>
    <a href="#dryrun" title="DryRun">DryRun</a>: <i>Boolean</i>
    <a href="#payer" title="Payer">Payer</a>: <i>String</i>
    <a href="#servicedescription" title="ServiceDescription">ServiceDescription</a>: <i>String</i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### AutoAcceptConnection

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConnectBandwidth

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DryRun

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Payer

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServiceDescription

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeoutsdefinition.md">TimeoutsDefinition</a>

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

#### ServiceBusinessStatus

Returns the <code>ServiceBusinessStatus</code> value.

#### ServiceDomain

Returns the <code>ServiceDomain</code> value.

#### Status

Returns the <code>Status</code> value.

