# TF::Quorum::BootstrapIstanbulExtradata

Use this resource to construct `extradata` field used in the genesis file.

`istanbul_address` can be referenced from `quorum_bootstrap_node_key` data source or newly created from `quorum_bootstrap_node_key` resources.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Quorum::BootstrapIstanbulExtradata",
    "Properties" : {
        "<a href="#istanbuladdresses" title="IstanbulAddresses">IstanbulAddresses</a>" : <i>[ String, ... ]</i>,
        "<a href="#mode" title="Mode">Mode</a>" : <i>String</i>,
        "<a href="#vanity" title="Vanity">Vanity</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Quorum::BootstrapIstanbulExtradata
Properties:
    <a href="#istanbuladdresses" title="IstanbulAddresses">IstanbulAddresses</a>: <i>
      - String</i>
    <a href="#mode" title="Mode">Mode</a>: <i>String</i>
    <a href="#vanity" title="Vanity">Vanity</a>: <i>String</i>
</pre>

## Properties

#### IstanbulAddresses

list of Istanbul address to construct extradata
- `mode` - (Optional) generate extradata using RLP encoding mode. Supported: ibft1, ibft2 and qbft. Default is ibft1
- `vanity` - (Optional) Vanity Hex Value to be included in the extradata.

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Mode

generate extradata using RLP encoding mode. Supported: ibft1, ibft2 and qbft. Default is ibft1
- `vanity` - (Optional) Vanity Hex Value to be included in the extradata.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vanity

Vanity Hex Value to be included in the extradata.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Extradata

Returns the <code>Extradata</code> value.

#### Id

Returns the <code>Id</code> value.

