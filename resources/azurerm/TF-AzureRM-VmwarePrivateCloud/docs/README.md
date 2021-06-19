# TF::AzureRM::VmwarePrivateCloud

Manages a Vmware Private Cloud.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AzureRM::VmwarePrivateCloud",
    "Properties" : {
        "<a href="#internetconnectionenabled" title="InternetConnectionEnabled">InternetConnectionEnabled</a>" : <i>Boolean</i>,
        "<a href="#location" title="Location">Location</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#networksubnetcidr" title="NetworkSubnetCidr">NetworkSubnetCidr</a>" : <i>String</i>,
        "<a href="#nsxtpassword" title="NsxtPassword">NsxtPassword</a>" : <i>String</i>,
        "<a href="#resourcegroupname" title="ResourceGroupName">ResourceGroupName</a>" : <i>String</i>,
        "<a href="#skuname" title="SkuName">SkuName</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tagsdefinition.md">TagsDefinition</a>, ... ]</i>,
        "<a href="#vcenterpassword" title="VcenterPassword">VcenterPassword</a>" : <i>String</i>,
        "<a href="#managementcluster" title="ManagementCluster">ManagementCluster</a>" : <i>[ <a href="managementclusterdefinition.md">ManagementClusterDefinition</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AzureRM::VmwarePrivateCloud
Properties:
    <a href="#internetconnectionenabled" title="InternetConnectionEnabled">InternetConnectionEnabled</a>: <i>Boolean</i>
    <a href="#location" title="Location">Location</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#networksubnetcidr" title="NetworkSubnetCidr">NetworkSubnetCidr</a>: <i>String</i>
    <a href="#nsxtpassword" title="NsxtPassword">NsxtPassword</a>: <i>String</i>
    <a href="#resourcegroupname" title="ResourceGroupName">ResourceGroupName</a>: <i>String</i>
    <a href="#skuname" title="SkuName">SkuName</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tagsdefinition.md">TagsDefinition</a></i>
    <a href="#vcenterpassword" title="VcenterPassword">VcenterPassword</a>: <i>String</i>
    <a href="#managementcluster" title="ManagementCluster">ManagementCluster</a>: <i>
      - <a href="managementclusterdefinition.md">ManagementClusterDefinition</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### InternetConnectionEnabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Location

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetworkSubnetCidr

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NsxtPassword

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResourceGroupName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SkuName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

_Required_: No

_Type_: List of <a href="tagsdefinition.md">TagsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VcenterPassword

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ManagementCluster

_Required_: No

_Type_: List of <a href="managementclusterdefinition.md">ManagementClusterDefinition</a>

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

#### Circuit

Returns the <code>Circuit</code> value.

#### HcxCloudManagerEndpoint

Returns the <code>HcxCloudManagerEndpoint</code> value.

#### Id

Returns the <code>Id</code> value.

#### ManagementSubnetCidr

Returns the <code>ManagementSubnetCidr</code> value.

#### NsxtCertificateThumbprint

Returns the <code>NsxtCertificateThumbprint</code> value.

#### NsxtManagerEndpoint

Returns the <code>NsxtManagerEndpoint</code> value.

#### ProvisioningSubnetCidr

Returns the <code>ProvisioningSubnetCidr</code> value.

#### VcenterCertificateThumbprint

Returns the <code>VcenterCertificateThumbprint</code> value.

#### VcsaEndpoint

Returns the <code>VcsaEndpoint</code> value.

#### VmotionSubnetCidr

Returns the <code>VmotionSubnetCidr</code> value.

