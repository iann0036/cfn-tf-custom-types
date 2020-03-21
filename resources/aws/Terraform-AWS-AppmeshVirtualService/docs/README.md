# Terraform::AWS::AppmeshVirtualService

CloudFormation equivalent of aws_appmesh_virtual_service

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AWS::AppmeshVirtualService",
    "Properties" : {
        "<a href="#id" title="Id">Id</a>" : <i>String</i>,
        "<a href="#meshname" title="MeshName">MeshName</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ &lt;a href=&#34;tags.md&#34;&gt;Tags&lt;/a&gt;, ... ]</i>,
        "<a href="#spec" title="Spec">Spec</a>" : <i>[ &lt;a href=&#34;spec.md&#34;&gt;Spec&lt;/a&gt;, ... ]</i>,
        "<a href="#provider" title="Provider">Provider</a>" : <i>[ &lt;a href=&#34;provider.md&#34;&gt;Provider&lt;/a&gt;, ... ]</i>,
        "<a href="#virtualnode" title="VirtualNode">VirtualNode</a>" : <i>[ &lt;a href=&#34;virtualnode.md&#34;&gt;VirtualNode&lt;/a&gt;, ... ]</i>,
        "<a href="#virtualrouter" title="VirtualRouter">VirtualRouter</a>" : <i>[ &lt;a href=&#34;virtualrouter.md&#34;&gt;VirtualRouter&lt;/a&gt;, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AWS::AppmeshVirtualService
Properties:
    <a href="#id" title="Id">Id</a>: <i>String</i>
    <a href="#meshname" title="MeshName">MeshName</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - &lt;a href=&#34;tags.md&#34;&gt;Tags&lt;/a&gt;</i>
    <a href="#spec" title="Spec">Spec</a>: <i>
      - &lt;a href=&#34;spec.md&#34;&gt;Spec&lt;/a&gt;</i>
    <a href="#provider" title="Provider">Provider</a>: <i>
      - &lt;a href=&#34;provider.md&#34;&gt;Provider&lt;/a&gt;</i>
    <a href="#virtualnode" title="VirtualNode">VirtualNode</a>: <i>
      - &lt;a href=&#34;virtualnode.md&#34;&gt;VirtualNode&lt;/a&gt;</i>
    <a href="#virtualrouter" title="VirtualRouter">VirtualRouter</a>: <i>
      - &lt;a href=&#34;virtualrouter.md&#34;&gt;VirtualRouter&lt;/a&gt;</i>
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

#### Spec

_Required_: No

_Type_: List of &lt;a href=&#34;spec.md&#34;&gt;Spec&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Provider

_Required_: No

_Type_: List of &lt;a href=&#34;provider.md&#34;&gt;Provider&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VirtualNode

_Required_: No

_Type_: List of &lt;a href=&#34;virtualnode.md&#34;&gt;VirtualNode&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VirtualRouter

_Required_: No

_Type_: List of &lt;a href=&#34;virtualrouter.md&#34;&gt;VirtualRouter&lt;/a&gt;

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

