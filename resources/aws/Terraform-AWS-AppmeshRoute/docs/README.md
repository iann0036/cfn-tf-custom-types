# Terraform::AWS::AppmeshRoute

CloudFormation equivalent of aws_appmesh_route

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AWS::AppmeshRoute",
    "Properties" : {
        "<a href="#id" title="Id">Id</a>" : <i>String</i>,
        "<a href="#meshname" title="MeshName">MeshName</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ &lt;a href=&#34;tags.md&#34;&gt;Tags&lt;/a&gt;, ... ]</i>,
        "<a href="#virtualroutername" title="VirtualRouterName">VirtualRouterName</a>" : <i>String</i>,
        "<a href="#spec" title="Spec">Spec</a>" : <i>[ &lt;a href=&#34;spec.md&#34;&gt;Spec&lt;/a&gt;, ... ]</i>,
        "<a href="#httproute" title="HttpRoute">HttpRoute</a>" : <i>[ &lt;a href=&#34;httproute.md&#34;&gt;HttpRoute&lt;/a&gt;, ... ]</i>,
        "<a href="#tcproute" title="TcpRoute">TcpRoute</a>" : <i>[ &lt;a href=&#34;tcproute.md&#34;&gt;TcpRoute&lt;/a&gt;, ... ]</i>,
        "<a href="#action" title="Action">Action</a>" : <i>[ &lt;a href=&#34;action.md&#34;&gt;Action&lt;/a&gt;, ... ]</i>,
        "<a href="#match" title="Match">Match</a>" : <i>[ &lt;a href=&#34;match.md&#34;&gt;Match&lt;/a&gt;, ... ]</i>,
        "<a href="#weightedtarget" title="WeightedTarget">WeightedTarget</a>" : <i>[ &lt;a href=&#34;weightedtarget.md&#34;&gt;WeightedTarget&lt;/a&gt;, ... ]</i>,
        "<a href="#header" title="Header">Header</a>" : <i>[ &lt;a href=&#34;header.md&#34;&gt;Header&lt;/a&gt;, ... ]</i>,
        "<a href="#range" title="Range">Range</a>" : <i>[ &lt;a href=&#34;range.md&#34;&gt;Range&lt;/a&gt;, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AWS::AppmeshRoute
Properties:
    <a href="#id" title="Id">Id</a>: <i>String</i>
    <a href="#meshname" title="MeshName">MeshName</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - &lt;a href=&#34;tags.md&#34;&gt;Tags&lt;/a&gt;</i>
    <a href="#virtualroutername" title="VirtualRouterName">VirtualRouterName</a>: <i>String</i>
    <a href="#spec" title="Spec">Spec</a>: <i>
      - &lt;a href=&#34;spec.md&#34;&gt;Spec&lt;/a&gt;</i>
    <a href="#httproute" title="HttpRoute">HttpRoute</a>: <i>
      - &lt;a href=&#34;httproute.md&#34;&gt;HttpRoute&lt;/a&gt;</i>
    <a href="#tcproute" title="TcpRoute">TcpRoute</a>: <i>
      - &lt;a href=&#34;tcproute.md&#34;&gt;TcpRoute&lt;/a&gt;</i>
    <a href="#action" title="Action">Action</a>: <i>
      - &lt;a href=&#34;action.md&#34;&gt;Action&lt;/a&gt;</i>
    <a href="#match" title="Match">Match</a>: <i>
      - &lt;a href=&#34;match.md&#34;&gt;Match&lt;/a&gt;</i>
    <a href="#weightedtarget" title="WeightedTarget">WeightedTarget</a>: <i>
      - &lt;a href=&#34;weightedtarget.md&#34;&gt;WeightedTarget&lt;/a&gt;</i>
    <a href="#header" title="Header">Header</a>: <i>
      - &lt;a href=&#34;header.md&#34;&gt;Header&lt;/a&gt;</i>
    <a href="#range" title="Range">Range</a>: <i>
      - &lt;a href=&#34;range.md&#34;&gt;Range&lt;/a&gt;</i>
</pre>

## Properties

#### Id

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MeshName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

_Required_: No

_Type_: List of &lt;a href=&#34;tags.md&#34;&gt;Tags&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VirtualRouterName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Spec

_Required_: No

_Type_: List of &lt;a href=&#34;spec.md&#34;&gt;Spec&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HttpRoute

_Required_: No

_Type_: List of &lt;a href=&#34;httproute.md&#34;&gt;HttpRoute&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TcpRoute

_Required_: No

_Type_: List of &lt;a href=&#34;tcproute.md&#34;&gt;TcpRoute&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Action

_Required_: No

_Type_: List of &lt;a href=&#34;action.md&#34;&gt;Action&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Match

_Required_: No

_Type_: List of &lt;a href=&#34;match.md&#34;&gt;Match&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WeightedTarget

_Required_: No

_Type_: List of &lt;a href=&#34;weightedtarget.md&#34;&gt;WeightedTarget&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Header

_Required_: No

_Type_: List of &lt;a href=&#34;header.md&#34;&gt;Header&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Range

_Required_: No

_Type_: List of &lt;a href=&#34;range.md&#34;&gt;Range&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Arn

Returns the &lt;code&gt;Arn&lt;/code&gt; value.

#### CreatedDate

Returns the &lt;code&gt;CreatedDate&lt;/code&gt; value.

#### LastUpdatedDate

Returns the &lt;code&gt;LastUpdatedDate&lt;/code&gt; value.

