# Terraform::AzureRM::PrivateLinkService

Manages a Private Link Service.

-> **NOTE** Private Link is now in [GA](https://docs.microsoft.com/en-gb/azure/private-link/).

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AzureRM::PrivateLinkService",
    "Properties" : {
        "<a href="#autoapprovalsubscriptionids" title="AutoApprovalSubscriptionIds">AutoApprovalSubscriptionIds</a>" : <i>[ String, ... ]</i>,
        "<a href="#enableproxyprotocol" title="EnableProxyProtocol">EnableProxyProtocol</a>" : <i>Boolean</i>,
        "<a href="#loadbalancerfrontendipconfigurationids" title="LoadBalancerFrontendIpConfigurationIds">LoadBalancerFrontendIpConfigurationIds</a>" : <i>[ String, ... ]</i>,
        "<a href="#location" title="Location">Location</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#resourcegroupname" title="ResourceGroupName">ResourceGroupName</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tags.md">Tags</a>, ... ]</i>,
        "<a href="#visibilitysubscriptionids" title="VisibilitySubscriptionIds">VisibilitySubscriptionIds</a>" : <i>[ String, ... ]</i>,
        "<a href="#natipconfiguration" title="NatIpConfiguration">NatIpConfiguration</a>" : <i>[ <a href="natipconfiguration.md">NatIpConfiguration</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeouts.md">Timeouts</a></i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AzureRM::PrivateLinkService
Properties:
    <a href="#autoapprovalsubscriptionids" title="AutoApprovalSubscriptionIds">AutoApprovalSubscriptionIds</a>: <i>
      - String</i>
    <a href="#enableproxyprotocol" title="EnableProxyProtocol">EnableProxyProtocol</a>: <i>Boolean</i>
    <a href="#loadbalancerfrontendipconfigurationids" title="LoadBalancerFrontendIpConfigurationIds">LoadBalancerFrontendIpConfigurationIds</a>: <i>
      - String</i>
    <a href="#location" title="Location">Location</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#resourcegroupname" title="ResourceGroupName">ResourceGroupName</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tags.md">Tags</a></i>
    <a href="#visibilitysubscriptionids" title="VisibilitySubscriptionIds">VisibilitySubscriptionIds</a>: <i>
      - String</i>
    <a href="#natipconfiguration" title="NatIpConfiguration">NatIpConfiguration</a>: <i>
      - <a href="natipconfiguration.md">NatIpConfiguration</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeouts.md">Timeouts</a></i>
</pre>

## Properties

#### AutoApprovalSubscriptionIds

A list of Subscription UUID/GUID's that will be automatically be able to use this Private Link Service.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableProxyProtocol

Should the Private Link Service support the Proxy Protocol? Defaults to `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LoadBalancerFrontendIpConfigurationIds

A list of Frontend IP Configuration ID's from a Standard Load Balancer, where traffic from the Private Link Service should be routed. You can use Load Balancer Rules to direct this traffic to appropriate backend pools where your applications are running.

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Location

Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Specifies the name of this Private Link Service. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResourceGroupName

The name of the Resource Group where the Private Link Service should exist. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

A mapping of tags to assign to the resource. Changing this forces a new resource to be created.

_Required_: No

_Type_: List of <a href="tags.md">Tags</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VisibilitySubscriptionIds

A list of Subscription UUID/GUID's that will be able to see this Private Link Service.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NatIpConfiguration

_Required_: No

_Type_: List of <a href="natipconfiguration.md">NatIpConfiguration</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeouts.md">Timeouts</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Alias

Returns the <code>Alias</code> value.

#### Id

Returns the <code>Id</code> value.

