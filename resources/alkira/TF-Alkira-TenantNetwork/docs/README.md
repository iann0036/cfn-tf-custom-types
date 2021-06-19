# TF::Alkira::TenantNetwork

CloudFormation equivalent of alkira_tenant_network

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Alkira::TenantNetwork",
    "Properties" : {
        "<a href="#connectors" title="Connectors">Connectors</a>" : <i>[ String, ... ]</i>,
        "<a href="#segments" title="Segments">Segments</a>" : <i>[ String, ... ]</i>,
        "<a href="#services" title="Services">Services</a>" : <i>[ String, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Alkira::TenantNetwork
Properties:
    <a href="#connectors" title="Connectors">Connectors</a>: <i>
      - String</i>
    <a href="#segments" title="Segments">Segments</a>: <i>
      - String</i>
    <a href="#services" title="Services">Services</a>: <i>
      - String</i>
</pre>

## Properties

#### Connectors

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Segments

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Services

_Required_: No

_Type_: List of String

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

