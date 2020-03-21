# Terraform::Panos::PanoramaPbfRuleGroup Forwarding

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#action" title="Action">Action</a>" : <i>String</i>,
    "<a href="#egressinterface" title="EgressInterface">EgressInterface</a>" : <i>String</i>,
    "<a href="#nexthoptype" title="NextHopType">NextHopType</a>" : <i>String</i>,
    "<a href="#nexthopvalue" title="NextHopValue">NextHopValue</a>" : <i>String</i>,
    "<a href="#vsys" title="Vsys">Vsys</a>" : <i>String</i>,
    "<a href="#monitor" title="Monitor">Monitor</a>" : <i>[ &lt;a href=&#34;forwarding-monitor.md&#34;&gt;Monitor&lt;/a&gt;, ... ]</i>,
    "<a href="#symmetricreturn" title="SymmetricReturn">SymmetricReturn</a>" : <i>[ &lt;a href=&#34;forwarding-symmetricreturn.md&#34;&gt;SymmetricReturn&lt;/a&gt;, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#action" title="Action">Action</a>: <i>String</i>
<a href="#egressinterface" title="EgressInterface">EgressInterface</a>: <i>String</i>
<a href="#nexthoptype" title="NextHopType">NextHopType</a>: <i>String</i>
<a href="#nexthopvalue" title="NextHopValue">NextHopValue</a>: <i>String</i>
<a href="#vsys" title="Vsys">Vsys</a>: <i>String</i>
<a href="#monitor" title="Monitor">Monitor</a>: <i>
      - &lt;a href=&#34;forwarding-monitor.md&#34;&gt;Monitor&lt;/a&gt;</i>
<a href="#symmetricreturn" title="SymmetricReturn">SymmetricReturn</a>: <i>
      - &lt;a href=&#34;forwarding-symmetricreturn.md&#34;&gt;SymmetricReturn&lt;/a&gt;</i>
</pre>

## Properties

#### Action

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EgressInterface

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NextHopType

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NextHopValue

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vsys

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Monitor

_Required_: No
_Type_: List of &lt;a href=&#34;forwarding-monitor.md&#34;&gt;Monitor&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SymmetricReturn

_Required_: No
_Type_: List of &lt;a href=&#34;forwarding-symmetricreturn.md&#34;&gt;SymmetricReturn&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

