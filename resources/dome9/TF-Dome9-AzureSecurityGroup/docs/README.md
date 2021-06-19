# TF::Dome9::AzureSecurityGroup

The Azure Security Group resource has methods to add and manage Azure Security Group policies for Azure cloud accounts that are managed by Dome9.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Dome9::AzureSecurityGroup",
    "Properties" : {
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#dome9cloudaccountid" title="Dome9CloudAccountId">Dome9CloudAccountId</a>" : <i>String</i>,
        "<a href="#dome9securitygroupname" title="Dome9SecurityGroupName">Dome9SecurityGroupName</a>" : <i>String</i>,
        "<a href="#istamperprotected" title="IsTamperProtected">IsTamperProtected</a>" : <i>Boolean</i>,
        "<a href="#region" title="Region">Region</a>" : <i>String</i>,
        "<a href="#resourcegroup" title="ResourceGroup">ResourceGroup</a>" : <i>String</i>,
        "<a href="#inbound" title="Inbound">Inbound</a>" : <i>[ <a href="inbounddefinition.md">InboundDefinition</a>, ... ]</i>,
        "<a href="#outbound" title="Outbound">Outbound</a>" : <i>[ <a href="outbounddefinition.md">OutboundDefinition</a>, ... ]</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tagsdefinition.md">TagsDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Dome9::AzureSecurityGroup
Properties:
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#dome9cloudaccountid" title="Dome9CloudAccountId">Dome9CloudAccountId</a>: <i>String</i>
    <a href="#dome9securitygroupname" title="Dome9SecurityGroupName">Dome9SecurityGroupName</a>: <i>String</i>
    <a href="#istamperprotected" title="IsTamperProtected">IsTamperProtected</a>: <i>Boolean</i>
    <a href="#region" title="Region">Region</a>: <i>String</i>
    <a href="#resourcegroup" title="ResourceGroup">ResourceGroup</a>: <i>String</i>
    <a href="#inbound" title="Inbound">Inbound</a>: <i>
      - <a href="inbounddefinition.md">InboundDefinition</a></i>
    <a href="#outbound" title="Outbound">Outbound</a>: <i>
      - <a href="outbounddefinition.md">OutboundDefinition</a></i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tagsdefinition.md">TagsDefinition</a></i>
</pre>

## Properties

#### Description

Service description.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Dome9CloudAccountId

Cloud account id in Dome9.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Dome9SecurityGroupName

Name of the security group.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IsTamperProtected

Is security group tamper protected.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Region

Region can be one of the following: `centralus`, `eastus`, `eastus2`, `usgovlowa`, `usgovvirginia`, `northcentralus`, `southcentralus`, `westus`, `westus2`, `westcentralus`, `northeurope`, `westeurope`, `eastasia`, `southeastasia`, `japaneast`, `japanwest`, `brazilsouth`, `australiaeast`, `australiasoutheast`, `centralindia`, `southindia`, `westindia`, `chinaeast`, `chinanorth`, `canadacentral`, `canadaeast`, `germanycentral`, `germanynortheast`, `koreacentral`, `uksouth`, `ukwest`, `koreasout`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResourceGroup

Azure resource group name.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Inbound

_Required_: No

_Type_: List of <a href="inbounddefinition.md">InboundDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Outbound

_Required_: No

_Type_: List of <a href="outbounddefinition.md">OutboundDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

_Required_: No

_Type_: List of <a href="tagsdefinition.md">TagsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### CloudAccountName

Returns the <code>CloudAccountName</code> value.

#### ExternalSecurityGroupId

Returns the <code>ExternalSecurityGroupId</code> value.

#### Id

Returns the <code>Id</code> value.

#### LastUpdatedByDome9

Returns the <code>LastUpdatedByDome9</code> value.

