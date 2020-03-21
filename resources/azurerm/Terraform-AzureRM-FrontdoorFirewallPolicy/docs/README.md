# Terraform::AzureRM::FrontdoorFirewallPolicy

CloudFormation equivalent of azurerm_frontdoor_firewall_policy

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AzureRM::FrontdoorFirewallPolicy",
    "Properties" : {
        "<a href="#customblockresponsebody" title="CustomBlockResponseBody">CustomBlockResponseBody</a>" : <i>String</i>,
        "<a href="#customblockresponsestatuscode" title="CustomBlockResponseStatusCode">CustomBlockResponseStatusCode</a>" : <i>Double</i>,
        "<a href="#enabled" title="Enabled">Enabled</a>" : <i>Boolean</i>,
        "<a href="#id" title="Id">Id</a>" : <i>String</i>,
        "<a href="#mode" title="Mode">Mode</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#redirecturl" title="RedirectUrl">RedirectUrl</a>" : <i>String</i>,
        "<a href="#resourcegroupname" title="ResourceGroupName">ResourceGroupName</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ &lt;a href=&#34;tags.md&#34;&gt;Tags&lt;/a&gt;, ... ]</i>,
        "<a href="#customrule" title="CustomRule">CustomRule</a>" : <i>[ &lt;a href=&#34;customrule.md&#34;&gt;CustomRule&lt;/a&gt;, ... ]</i>,
        "<a href="#managedrule" title="ManagedRule">ManagedRule</a>" : <i>[ &lt;a href=&#34;managedrule.md&#34;&gt;ManagedRule&lt;/a&gt;, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i>&lt;a href=&#34;timeouts.md&#34;&gt;Timeouts&lt;/a&gt;</i>,
        "<a href="#matchcondition" title="MatchCondition">MatchCondition</a>" : <i>[ &lt;a href=&#34;matchcondition.md&#34;&gt;MatchCondition&lt;/a&gt;, ... ]</i>,
        "<a href="#exclusion" title="Exclusion">Exclusion</a>" : <i>[ &lt;a href=&#34;exclusion.md&#34;&gt;Exclusion&lt;/a&gt;, ... ]</i>,
        "<a href="#override" title="Override">Override</a>" : <i>[ &lt;a href=&#34;override.md&#34;&gt;Override&lt;/a&gt;, ... ]</i>,
        "<a href="#rule" title="Rule">Rule</a>" : <i>[ &lt;a href=&#34;rule.md&#34;&gt;Rule&lt;/a&gt;, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AzureRM::FrontdoorFirewallPolicy
Properties:
    <a href="#customblockresponsebody" title="CustomBlockResponseBody">CustomBlockResponseBody</a>: <i>String</i>
    <a href="#customblockresponsestatuscode" title="CustomBlockResponseStatusCode">CustomBlockResponseStatusCode</a>: <i>Double</i>
    <a href="#enabled" title="Enabled">Enabled</a>: <i>Boolean</i>
    <a href="#id" title="Id">Id</a>: <i>String</i>
    <a href="#mode" title="Mode">Mode</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#redirecturl" title="RedirectUrl">RedirectUrl</a>: <i>String</i>
    <a href="#resourcegroupname" title="ResourceGroupName">ResourceGroupName</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - &lt;a href=&#34;tags.md&#34;&gt;Tags&lt;/a&gt;</i>
    <a href="#customrule" title="CustomRule">CustomRule</a>: <i>
      - &lt;a href=&#34;customrule.md&#34;&gt;CustomRule&lt;/a&gt;</i>
    <a href="#managedrule" title="ManagedRule">ManagedRule</a>: <i>
      - &lt;a href=&#34;managedrule.md&#34;&gt;ManagedRule&lt;/a&gt;</i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i>&lt;a href=&#34;timeouts.md&#34;&gt;Timeouts&lt;/a&gt;</i>
    <a href="#matchcondition" title="MatchCondition">MatchCondition</a>: <i>
      - &lt;a href=&#34;matchcondition.md&#34;&gt;MatchCondition&lt;/a&gt;</i>
    <a href="#exclusion" title="Exclusion">Exclusion</a>: <i>
      - &lt;a href=&#34;exclusion.md&#34;&gt;Exclusion&lt;/a&gt;</i>
    <a href="#override" title="Override">Override</a>: <i>
      - &lt;a href=&#34;override.md&#34;&gt;Override&lt;/a&gt;</i>
    <a href="#rule" title="Rule">Rule</a>: <i>
      - &lt;a href=&#34;rule.md&#34;&gt;Rule&lt;/a&gt;</i>
</pre>

## Properties

#### CustomBlockResponseBody

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CustomBlockResponseStatusCode

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Enabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Id

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Mode

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RedirectUrl

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResourceGroupName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

_Required_: No

_Type_: List of &lt;a href=&#34;tags.md&#34;&gt;Tags&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CustomRule

_Required_: No

_Type_: List of &lt;a href=&#34;customrule.md&#34;&gt;CustomRule&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ManagedRule

_Required_: No

_Type_: List of &lt;a href=&#34;managedrule.md&#34;&gt;ManagedRule&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: &lt;a href=&#34;timeouts.md&#34;&gt;Timeouts&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MatchCondition

_Required_: No

_Type_: List of &lt;a href=&#34;matchcondition.md&#34;&gt;MatchCondition&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Exclusion

_Required_: No

_Type_: List of &lt;a href=&#34;exclusion.md&#34;&gt;Exclusion&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Override

_Required_: No

_Type_: List of &lt;a href=&#34;override.md&#34;&gt;Override&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Rule

_Required_: No

_Type_: List of &lt;a href=&#34;rule.md&#34;&gt;Rule&lt;/a&gt;

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

Returns the &lt;code&gt;FrontendEndpointIds&lt;/code&gt; value.

#### Location

Returns the &lt;code&gt;Location&lt;/code&gt; value.

