# Terraform::Alicloud::NetworkAclEntries

CloudFormation equivalent of alicloud_network_acl_entries

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Alicloud::NetworkAclEntries",
    "Properties" : {
        "<a href="#id" title="Id">Id</a>" : <i>String</i>,
        "<a href="#networkaclid" title="NetworkAclId">NetworkAclId</a>" : <i>String</i>,
        "<a href="#egress" title="Egress">Egress</a>" : <i>[ &lt;a href=&#34;egress.md&#34;&gt;Egress&lt;/a&gt;, ... ]</i>,
        "<a href="#ingress" title="Ingress">Ingress</a>" : <i>[ &lt;a href=&#34;ingress.md&#34;&gt;Ingress&lt;/a&gt;, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Alicloud::NetworkAclEntries
Properties:
    <a href="#id" title="Id">Id</a>: <i>String</i>
    <a href="#networkaclid" title="NetworkAclId">NetworkAclId</a>: <i>String</i>
    <a href="#egress" title="Egress">Egress</a>: <i>
      - &lt;a href=&#34;egress.md&#34;&gt;Egress&lt;/a&gt;</i>
    <a href="#ingress" title="Ingress">Ingress</a>: <i>
      - &lt;a href=&#34;ingress.md&#34;&gt;Ingress&lt;/a&gt;</i>
</pre>

## Properties

#### Id

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetworkAclId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Egress

_Required_: No

_Type_: List of &lt;a href=&#34;egress.md&#34;&gt;Egress&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ingress

_Required_: No

_Type_: List of &lt;a href=&#34;ingress.md&#34;&gt;Ingress&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

