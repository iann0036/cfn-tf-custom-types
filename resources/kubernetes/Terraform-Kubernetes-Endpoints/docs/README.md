# Terraform::Kubernetes::Endpoints

CloudFormation equivalent of kubernetes_endpoints

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Kubernetes::Endpoints",
    "Properties" : {
        "<a href="#tfcfnid" title="tfcfnid">tfcfnid</a>" : <i>String</i>,
        "<a href="#metadata" title="Metadata">Metadata</a>" : <i>[ &lt;a href=&#34;metadata.md&#34;&gt;Metadata&lt;/a&gt;, ... ]</i>,
        "<a href="#subset" title="Subset">Subset</a>" : <i>[ &lt;a href=&#34;subset.md&#34;&gt;Subset&lt;/a&gt;, ... ]</i>,
        "<a href="#address" title="Address">Address</a>" : <i>[ &lt;a href=&#34;address.md&#34;&gt;Address&lt;/a&gt;, ... ]</i>,
        "<a href="#notreadyaddress" title="NotReadyAddress">NotReadyAddress</a>" : <i>[ &lt;a href=&#34;notreadyaddress.md&#34;&gt;NotReadyAddress&lt;/a&gt;, ... ]</i>,
        "<a href="#port" title="Port">Port</a>" : <i>[ &lt;a href=&#34;port.md&#34;&gt;Port&lt;/a&gt;, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Kubernetes::Endpoints
Properties:
    <a href="#tfcfnid" title="tfcfnid">tfcfnid</a>: <i>String</i>
    <a href="#metadata" title="Metadata">Metadata</a>: <i>
      - &lt;a href=&#34;metadata.md&#34;&gt;Metadata&lt;/a&gt;</i>
    <a href="#subset" title="Subset">Subset</a>: <i>
      - &lt;a href=&#34;subset.md&#34;&gt;Subset&lt;/a&gt;</i>
    <a href="#address" title="Address">Address</a>: <i>
      - &lt;a href=&#34;address.md&#34;&gt;Address&lt;/a&gt;</i>
    <a href="#notreadyaddress" title="NotReadyAddress">NotReadyAddress</a>: <i>
      - &lt;a href=&#34;notreadyaddress.md&#34;&gt;NotReadyAddress&lt;/a&gt;</i>
    <a href="#port" title="Port">Port</a>: <i>
      - &lt;a href=&#34;port.md&#34;&gt;Port&lt;/a&gt;</i>
</pre>

## Properties

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Metadata

_Required_: No

_Type_: List of &lt;a href=&#34;metadata.md&#34;&gt;Metadata&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Subset

_Required_: No

_Type_: List of &lt;a href=&#34;subset.md&#34;&gt;Subset&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Address

_Required_: No

_Type_: List of &lt;a href=&#34;address.md&#34;&gt;Address&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NotReadyAddress

_Required_: No

_Type_: List of &lt;a href=&#34;notreadyaddress.md&#34;&gt;NotReadyAddress&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Port

_Required_: No

_Type_: List of &lt;a href=&#34;port.md&#34;&gt;Port&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

