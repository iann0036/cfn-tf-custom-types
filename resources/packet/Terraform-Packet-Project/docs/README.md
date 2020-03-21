# Terraform::Packet::Project

Provides a Packet project resource to allow you manage devices
in your projects.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Packet::Project",
    "Properties" : {
        "<a href="#backendtransfer" title="BackendTransfer">BackendTransfer</a>" : <i>Boolean</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#organizationid" title="OrganizationId">OrganizationId</a>" : <i>String</i>,
        "<a href="#paymentmethodid" title="PaymentMethodId">PaymentMethodId</a>" : <i>String</i>,
        "<a href="#bgpconfig" title="BgpConfig">BgpConfig</a>" : <i>[ <a href="bgpconfig.md">BgpConfig</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Packet::Project
Properties:
    <a href="#backendtransfer" title="BackendTransfer">BackendTransfer</a>: <i>Boolean</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#organizationid" title="OrganizationId">OrganizationId</a>: <i>String</i>
    <a href="#paymentmethodid" title="PaymentMethodId">PaymentMethodId</a>: <i>String</i>
    <a href="#bgpconfig" title="BgpConfig">BgpConfig</a>: <i>
      - <a href="bgpconfig.md">BgpConfig</a></i>
</pre>

## Properties

#### BackendTransfer

Enable or disable [Backend Transfer](https://www.packet.com/developers/docs/network/basic/backend-transfer/), default is false.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of the project.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OrganizationId

The UUID of organization under which you want to create the project. If you leave it out, the project will be create under your the default organization of your account.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PaymentMethodId

The UUID of payment method for this project. The payment method and the project need to belong to the same organization (passed with `organization_id`, or default).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BgpConfig

_Required_: No

_Type_: List of <a href="bgpconfig.md">BgpConfig</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Created

Returns the <code>Created</code> value.

#### Updated

Returns the <code>Updated</code> value.

