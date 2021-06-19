# TF::AzureRM::FrontdoorFirewallPolicy

Manages an Azure Front Door Web Application Firewall Policy instance.

!> **Be Aware:** Azure is rolling out a breaking change on Friday 9th April which may cause issues with the CDN/FrontDoor resources. [More information is available in this Github issue](https://github.com/terraform-providers/terraform-provider-azurerm/issues/11231) - however unfortunately this may necessitate a breaking change to the CDN and FrontDoor resources, more information will be posted [in the Github issue](https://github.com/terraform-providers/terraform-provider-azurerm/issues/11231) as the necessary changes are identified.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AzureRM::FrontdoorFirewallPolicy",
    "Properties" : {
        "<a href="#customblockresponsebody" title="CustomBlockResponseBody">CustomBlockResponseBody</a>" : <i>String</i>,
        "<a href="#customblockresponsestatuscode" title="CustomBlockResponseStatusCode">CustomBlockResponseStatusCode</a>" : <i>Double</i>,
        "<a href="#enabled" title="Enabled">Enabled</a>" : <i>Boolean</i>,
        "<a href="#mode" title="Mode">Mode</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#redirecturl" title="RedirectUrl">RedirectUrl</a>" : <i>String</i>,
        "<a href="#resourcegroupname" title="ResourceGroupName">ResourceGroupName</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tagsdefinition.md">TagsDefinition</a>, ... ]</i>,
        "<a href="#customrule" title="CustomRule">CustomRule</a>" : <i>[ <a href="customruledefinition.md">CustomRuleDefinition</a>, ... ]</i>,
        "<a href="#managedrule" title="ManagedRule">ManagedRule</a>" : <i>[ <a href="managedruledefinition.md">ManagedRuleDefinition</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AzureRM::FrontdoorFirewallPolicy
Properties:
    <a href="#customblockresponsebody" title="CustomBlockResponseBody">CustomBlockResponseBody</a>: <i>String</i>
    <a href="#customblockresponsestatuscode" title="CustomBlockResponseStatusCode">CustomBlockResponseStatusCode</a>: <i>Double</i>
    <a href="#enabled" title="Enabled">Enabled</a>: <i>Boolean</i>
    <a href="#mode" title="Mode">Mode</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#redirecturl" title="RedirectUrl">RedirectUrl</a>: <i>String</i>
    <a href="#resourcegroupname" title="ResourceGroupName">ResourceGroupName</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tagsdefinition.md">TagsDefinition</a></i>
    <a href="#customrule" title="CustomRule">CustomRule</a>: <i>
      - <a href="customruledefinition.md">CustomRuleDefinition</a></i>
    <a href="#managedrule" title="ManagedRule">ManagedRule</a>: <i>
      - <a href="managedruledefinition.md">ManagedRuleDefinition</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### CustomBlockResponseBody

If a `custom_rule` block's action type is `block`, this is the response body. The body must be specified in base64 encoding.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CustomBlockResponseStatusCode

If a `custom_rule` block's action type is `block`, this is the response status code. Possible values are `200`, `403`, `405`, `406`, or `429`.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Enabled

Is the policy a enabled state or disabled state. Defaults to `true`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Mode

The firewall policy mode. Possible values are `Detection`, `Prevention` and defaults to `Prevention`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of the policy. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RedirectUrl

If action type is redirect, this field represents redirect URL for the client.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResourceGroupName

The name of the resource group. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

A mapping of tags to assign to the Web Application Firewall Policy.

_Required_: No

_Type_: List of <a href="tagsdefinition.md">TagsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CustomRule

_Required_: No

_Type_: List of <a href="customruledefinition.md">CustomRuleDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ManagedRule

_Required_: No

_Type_: List of <a href="managedruledefinition.md">ManagedRuleDefinition</a>

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

#### FrontendEndpointIds

Returns the <code>FrontendEndpointIds</code> value.

#### Id

Returns the <code>Id</code> value.

#### Location

Returns the <code>Location</code> value.

