# Terraform::Alicloud::NetworkAclEntries

Provides a network acl entries resource to create ingress and egress entries.

-> **NOTE:** Available in 1.45.0+. Currently, the resource are only available in Hongkong(cn-hongkong), India(ap-south-1), and Indonesia(ap-southeast-1) regions.

-> **NOTE:** It doesn't support concurrency and the order of the ingress and egress entries determines the priority.

-> **NOTE:** Using this resource need to open a whitelist.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Alicloud::NetworkAclEntries",
    "Properties" : {
        "<a href="#networkaclid" title="NetworkAclId">NetworkAclId</a>" : <i>String</i>,
        "<a href="#egress" title="Egress">Egress</a>" : <i>[ <a href="egress.md">Egress</a>, ... ]</i>,
        "<a href="#ingress" title="Ingress">Ingress</a>" : <i>[ <a href="ingress.md">Ingress</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Alicloud::NetworkAclEntries
Properties:
    <a href="#networkaclid" title="NetworkAclId">NetworkAclId</a>: <i>String</i>
    <a href="#egress" title="Egress">Egress</a>: <i>
      - <a href="egress.md">Egress</a></i>
    <a href="#ingress" title="Ingress">Ingress</a>: <i>
      - <a href="ingress.md">Ingress</a></i>
</pre>

## Properties

#### NetworkAclId

The id of the network acl, the field can't be changed.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Egress

_Required_: No

_Type_: List of <a href="egress.md">Egress</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ingress

_Required_: No

_Type_: List of <a href="ingress.md">Ingress</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Id

Returns the <code>Id</code> value.

