# Terraform::AWS::CodedeployDeploymentGroup LoadBalancerInfo TargetGroupPairInfo

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#prodtrafficroute" title="ProdTrafficRoute">ProdTrafficRoute</a>" : <i>[ &lt;a href=&#34;loadbalancerinfo-targetgrouppairinfo-prodtrafficroute.md&#34;&gt;ProdTrafficRoute&lt;/a&gt;, ... ]</i>,
    "<a href="#targetgroup" title="TargetGroup">TargetGroup</a>" : <i>[ &lt;a href=&#34;loadbalancerinfo-targetgrouppairinfo-targetgroup.md&#34;&gt;TargetGroup&lt;/a&gt;, ... ]</i>,
    "<a href="#testtrafficroute" title="TestTrafficRoute">TestTrafficRoute</a>" : <i>[ &lt;a href=&#34;loadbalancerinfo-targetgrouppairinfo-testtrafficroute.md&#34;&gt;TestTrafficRoute&lt;/a&gt;, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#prodtrafficroute" title="ProdTrafficRoute">ProdTrafficRoute</a>: <i>
      - &lt;a href=&#34;loadbalancerinfo-targetgrouppairinfo-prodtrafficroute.md&#34;&gt;ProdTrafficRoute&lt;/a&gt;</i>
<a href="#targetgroup" title="TargetGroup">TargetGroup</a>: <i>
      - &lt;a href=&#34;loadbalancerinfo-targetgrouppairinfo-targetgroup.md&#34;&gt;TargetGroup&lt;/a&gt;</i>
<a href="#testtrafficroute" title="TestTrafficRoute">TestTrafficRoute</a>: <i>
      - &lt;a href=&#34;loadbalancerinfo-targetgrouppairinfo-testtrafficroute.md&#34;&gt;TestTrafficRoute&lt;/a&gt;</i>
</pre>

## Properties

#### ProdTrafficRoute

_Required_: No
_Type_: List of &lt;a href=&#34;loadbalancerinfo-targetgrouppairinfo-prodtrafficroute.md&#34;&gt;ProdTrafficRoute&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TargetGroup

_Required_: No
_Type_: List of &lt;a href=&#34;loadbalancerinfo-targetgrouppairinfo-targetgroup.md&#34;&gt;TargetGroup&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TestTrafficRoute

_Required_: No
_Type_: List of &lt;a href=&#34;loadbalancerinfo-targetgrouppairinfo-testtrafficroute.md&#34;&gt;TestTrafficRoute&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

