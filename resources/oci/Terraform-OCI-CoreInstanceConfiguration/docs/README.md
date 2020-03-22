# Terraform::OCI::CoreInstanceConfiguration

This resource provides the Instance Configuration resource in Oracle Cloud Infrastructure Core service.

Creates an instance configuration. An instance configuration is a template that defines the
settings to use when creating Compute instances.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::OCI::CoreInstanceConfiguration",
    "Properties" : {
        "<a href="#compartmentid" title="CompartmentId">CompartmentId</a>" : <i>String</i>,
        "<a href="#definedtags" title="DefinedTags">DefinedTags</a>" : <i>[ <a href="definedtags.md">DefinedTags</a>, ... ]</i>,
        "<a href="#displayname" title="DisplayName">DisplayName</a>" : <i>String</i>,
        "<a href="#freeformtags" title="FreeformTags">FreeformTags</a>" : <i>[ <a href="freeformtags.md">FreeformTags</a>, ... ]</i>,
        "<a href="#instanceid" title="InstanceId">InstanceId</a>" : <i>String</i>,
        "<a href="#source" title="Source">Source</a>" : <i>String</i>,
        "<a href="#instancedetails" title="InstanceDetails">InstanceDetails</a>" : <i>[ <a href="instancedetails.md">InstanceDetails</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeouts.md">Timeouts</a></i>,
        "<a href="#blockvolumes" title="BlockVolumes">BlockVolumes</a>" : <i>[ <a href="blockvolumes.md">BlockVolumes</a>, ... ]</i>,
        "<a href="#launchdetails" title="LaunchDetails">LaunchDetails</a>" : <i>[ <a href="launchdetails.md">LaunchDetails</a>, ... ]</i>,
        "<a href="#secondaryvnics" title="SecondaryVnics">SecondaryVnics</a>" : <i>[ <a href="secondaryvnics.md">SecondaryVnics</a>, ... ]</i>,
        "<a href="#attachdetails" title="AttachDetails">AttachDetails</a>" : <i>[ <a href="attachdetails.md">AttachDetails</a>, ... ]</i>,
        "<a href="#createdetails" title="CreateDetails">CreateDetails</a>" : <i>[ <a href="createdetails.md">CreateDetails</a>, ... ]</i>,
        "<a href="#createvnicdetails" title="CreateVnicDetails">CreateVnicDetails</a>" : <i>[ <a href="createvnicdetails.md">CreateVnicDetails</a>, ... ]</i>,
        "<a href="#sourcedetails" title="SourceDetails">SourceDetails</a>" : <i>[ <a href="sourcedetails.md">SourceDetails</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::OCI::CoreInstanceConfiguration
Properties:
    <a href="#compartmentid" title="CompartmentId">CompartmentId</a>: <i>String</i>
    <a href="#definedtags" title="DefinedTags">DefinedTags</a>: <i>
      - <a href="definedtags.md">DefinedTags</a></i>
    <a href="#displayname" title="DisplayName">DisplayName</a>: <i>String</i>
    <a href="#freeformtags" title="FreeformTags">FreeformTags</a>: <i>
      - <a href="freeformtags.md">FreeformTags</a></i>
    <a href="#instanceid" title="InstanceId">InstanceId</a>: <i>String</i>
    <a href="#source" title="Source">Source</a>: <i>String</i>
    <a href="#instancedetails" title="InstanceDetails">InstanceDetails</a>: <i>
      - <a href="instancedetails.md">InstanceDetails</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeouts.md">Timeouts</a></i>
    <a href="#blockvolumes" title="BlockVolumes">BlockVolumes</a>: <i>
      - <a href="blockvolumes.md">BlockVolumes</a></i>
    <a href="#launchdetails" title="LaunchDetails">LaunchDetails</a>: <i>
      - <a href="launchdetails.md">LaunchDetails</a></i>
    <a href="#secondaryvnics" title="SecondaryVnics">SecondaryVnics</a>: <i>
      - <a href="secondaryvnics.md">SecondaryVnics</a></i>
    <a href="#attachdetails" title="AttachDetails">AttachDetails</a>: <i>
      - <a href="attachdetails.md">AttachDetails</a></i>
    <a href="#createdetails" title="CreateDetails">CreateDetails</a>: <i>
      - <a href="createdetails.md">CreateDetails</a></i>
    <a href="#createvnicdetails" title="CreateVnicDetails">CreateVnicDetails</a>: <i>
      - <a href="createvnicdetails.md">CreateVnicDetails</a></i>
    <a href="#sourcedetails" title="SourceDetails">SourceDetails</a>: <i>
      - <a href="sourcedetails.md">SourceDetails</a></i>
</pre>

## Properties

#### CompartmentId

The OCID of the compartment.
* `create_vnic_details` - (Optional) Details for the primary VNIC, which is automatically created and attached when the instance is launched.
* `assign_public_ip` - (Optional) Whether the VNIC should be assigned a public IP address. See the `assignPublicIp` attribute of [CreateVnicDetails](https://docs.cloud.oracle.com/iaas/api/#/en/iaas/20160918/CreateVnicDetails/) for more information.
* `display_name` - (Optional) A user-friendly name for the VNIC. Does not have to be unique. Avoid entering confidential information.
* `hostname_label` - (Optional) The hostname for the VNIC's primary private IP. See the `hostnameLabel` attribute of [CreateVnicDetails](https://docs.cloud.oracle.com/iaas/api/#/en/iaas/20160918/CreateVnicDetails/) for more information.
* `nsg_ids` - (Optional) A list of the OCIDs of the network security groups (NSGs) to add the VNIC to. For more information about NSGs, see [NetworkSecurityGroup](https://docs.cloud.oracle.com/iaas/api/#/en/iaas/20160918/NetworkSecurityGroup/).
* `private_ip` - (Optional) A private IP address of your choice to assign to the VNIC. See the `privateIp` attribute of [CreateVnicDetails](https://docs.cloud.oracle.com/iaas/api/#/en/iaas/20160918/CreateVnicDetails/) for more information.
* `skip_source_dest_check` - (Optional) Whether the source/destination check is disabled on the VNIC. See the `skipSourceDestCheck` attribute of [CreateVnicDetails](https://docs.cloud.oracle.com/iaas/api/#/en/iaas/20160918/CreateVnicDetails/) for more information.
* `subnet_id` - (Optional) The OCID of the subnet to create the VNIC in. See the `subnetId` attribute of [CreateVnicDetails](https://docs.cloud.oracle.com/iaas/api/#/en/iaas/20160918/CreateVnicDetails/) for more information.
* `defined_tags` - (Optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Operations.CostCenter": "42"}`
* `display_name` - (Optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.  Example: `My bare metal instance`
* `extended_metadata` - (Optional) Additional metadata key/value pairs that you provide. They serve the same purpose and functionality as fields in the 'metadata' object.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefinedTags

Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Operations.CostCenter": "42"}`
* `display_name` - (Optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.  Example: `My bare metal instance`
* `extended_metadata` - (Optional) Additional metadata key/value pairs that you provide. They serve the same purpose and functionality as fields in the 'metadata' object.

_Required_: No

_Type_: List of <a href="definedtags.md">DefinedTags</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisplayName

A user-friendly name for the attachment. Does not have to be unique, and it cannot be changed.
* `nic_index` - (Optional) Which physical network interface card (NIC) the VNIC will use. Defaults to 0. Certain bare metal instance shapes have two active physical NICs (0 and 1). If you add a secondary VNIC to one of these instances, you can specify which NIC the VNIC will use. For more information, see [Virtual Network Interface Cards (VNICs)](https://docs.cloud.oracle.com/iaas/Content/Network/Tasks/managingVNICs.htm).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FreeformTags

Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Department": "Finance"}`
* `ipxe_script` - (Optional) This is an advanced option.

_Required_: No

_Type_: List of <a href="freeformtags.md">FreeformTags</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InstanceId

The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the instance to use to create the instance configuration.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Source

The source of the instance configuration. An instance configuration defines the settings to use when creating Compute instances, including details such as the base image, shape, and metadata. You can also specify the associated resources for the instance, such as block volume attachments and network configuration.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InstanceDetails

_Required_: No

_Type_: List of <a href="instancedetails.md">InstanceDetails</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeouts.md">Timeouts</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BlockVolumes

_Required_: No

_Type_: List of <a href="blockvolumes.md">BlockVolumes</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LaunchDetails

_Required_: No

_Type_: List of <a href="launchdetails.md">LaunchDetails</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecondaryVnics

_Required_: No

_Type_: List of <a href="secondaryvnics.md">SecondaryVnics</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AttachDetails

_Required_: No

_Type_: List of <a href="attachdetails.md">AttachDetails</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CreateDetails

_Required_: No

_Type_: List of <a href="createdetails.md">CreateDetails</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CreateVnicDetails

_Required_: No

_Type_: List of <a href="createvnicdetails.md">CreateVnicDetails</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceDetails

_Required_: No

_Type_: List of <a href="sourcedetails.md">SourceDetails</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### DeferredFields

Returns the <code>DeferredFields</code> value.

#### Id

The OCID of the volume backup.
* `type` - (Required) The type can be one of these values: `volume`, `volumeBackup`
* `volume_id` - (Optional) The OCID of the volume.
* `instance_type` - (Required) The type of instance details. Supported instanceType is compute
* `launch_details` - (Optional)
* `availability_domain` - (Optional) The availability domain of the instance.  Example: `Uocm:PHX-AD-1`
* `compartment_id` - (Optional) The OCID of the compartment.
* `create_vnic_details` - (Optional) Details for the primary VNIC, which is automatically created and attached when the instance is launched.
* `assign_public_ip` - (Optional) Whether the VNIC should be assigned a public IP address. See the `assignPublicIp` attribute of [CreateVnicDetails](https://docs.cloud.oracle.com/iaas/api/#/en/iaas/20160918/CreateVnicDetails/) for more information.
* `display_name` - (Optional) A user-friendly name for the VNIC. Does not have to be unique. Avoid entering confidential information.
* `hostname_label` - (Optional) The hostname for the VNIC's primary private IP. See the `hostnameLabel` attribute of [CreateVnicDetails](https://docs.cloud.oracle.com/iaas/api/#/en/iaas/20160918/CreateVnicDetails/) for more information.
* `nsg_ids` - (Optional) A list of the OCIDs of the network security groups (NSGs) to add the VNIC to. For more information about NSGs, see [NetworkSecurityGroup](https://docs.cloud.oracle.com/iaas/api/#/en/iaas/20160918/NetworkSecurityGroup/).
* `private_ip` - (Optional) A private IP address of your choice to assign to the VNIC. See the `privateIp` attribute of [CreateVnicDetails](https://docs.cloud.oracle.com/iaas/api/#/en/iaas/20160918/CreateVnicDetails/) for more information.
* `skip_source_dest_check` - (Optional) Whether the source/destination check is disabled on the VNIC. See the `skipSourceDestCheck` attribute of [CreateVnicDetails](https://docs.cloud.oracle.com/iaas/api/#/en/iaas/20160918/CreateVnicDetails/) for more information.
* `subnet_id` - (Optional) The OCID of the subnet to create the VNIC in. See the `subnetId` attribute of [CreateVnicDetails](https://docs.cloud.oracle.com/iaas/api/#/en/iaas/20160918/CreateVnicDetails/) for more information.
* `defined_tags` - (Optional) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Operations.CostCenter": "42"}`
* `display_name` - (Optional) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.  Example: `My bare metal instance`
* `extended_metadata` - (Optional) Additional metadata key/value pairs that you provide. They serve the same purpose and functionality as fields in the 'metadata' object.

#### TimeCreated

Returns the <code>TimeCreated</code> value.

