# Terraform::OCI::CoreVnicAttachment

This resource provides the Vnic Attachment resource in Oracle Cloud Infrastructure Core service.

Creates a secondary VNIC and attaches it to the specified instance.
For more information about secondary VNICs, see
[Virtual Network Interface Cards (VNICs)](https://docs.cloud.oracle.com/iaas/Content/Network/Tasks/managingVNICs.htm).

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::OCI::CoreVnicAttachment",
    "Properties" : {
        "<a href="#displayname" title="DisplayName">DisplayName</a>" : <i>String</i>,
        "<a href="#instanceid" title="InstanceId">InstanceId</a>" : <i>String</i>,
        "<a href="#nicindex" title="NicIndex">NicIndex</a>" : <i>Double</i>,
        "<a href="#createvnicdetails" title="CreateVnicDetails">CreateVnicDetails</a>" : <i>[ <a href="createvnicdetails.md">CreateVnicDetails</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeouts.md">Timeouts</a></i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::OCI::CoreVnicAttachment
Properties:
    <a href="#displayname" title="DisplayName">DisplayName</a>: <i>String</i>
    <a href="#instanceid" title="InstanceId">InstanceId</a>: <i>String</i>
    <a href="#nicindex" title="NicIndex">NicIndex</a>: <i>Double</i>
    <a href="#createvnicdetails" title="CreateVnicDetails">CreateVnicDetails</a>: <i>
      - <a href="createvnicdetails.md">CreateVnicDetails</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeouts.md">Timeouts</a></i>
</pre>

## Properties

#### DisplayName

A user-friendly name for the attachment. Does not have to be unique, and it cannot be changed. Avoid entering confidential information.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InstanceId

The OCID of the instance.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NicIndex

Which physical network interface card (NIC) the VNIC will use. Defaults to 0. Certain bare metal instance shapes have two active physical NICs (0 and 1). If you add a secondary VNIC to one of these instances, you can specify which NIC the VNIC will use. For more information, see [Virtual Network Interface Cards (VNICs)](https://docs.cloud.oracle.com/iaas/Content/Network/Tasks/managingVNICs.htm).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CreateVnicDetails

_Required_: No

_Type_: List of <a href="createvnicdetails.md">CreateVnicDetails</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeouts.md">Timeouts</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the Id.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### AvailabilityDomain

Returns the <code>AvailabilityDomain</code> value.

#### CompartmentId

Returns the <code>CompartmentId</code> value.

#### Id

Returns the <code>Id</code> value.

#### State

Returns the <code>State</code> value.

#### SubnetId

The OCID of the subnet to create the VNIC in. When launching an instance, use this `subnetId` instead of the deprecated `subnetId` in [LaunchInstanceDetails](https://docs.cloud.oracle.com/iaas/api/#/en/iaas/20160918/requests/LaunchInstanceDetails). Alternatively, the `vlanId` can be used instead of a `subnetId`. At least one `subnetId` value is required if this field is populated; if you provide both, the values must match. If both the `vlanId` and `subnetId` fields are provided, the launch will fail.

#### TimeCreated

Returns the <code>TimeCreated</code> value.

#### VlanTag

Returns the <code>VlanTag</code> value.

#### VnicId

Returns the <code>VnicId</code> value.

