# Terraform::Random::Id

CloudFormation equivalent of random_id

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Random::Id",
    "Properties" : {
        "<a href="#tfcfnid" title="tfcfnid">tfcfnid</a>" : <i>String</i>,
        "<a href="#b64" title="B64">B64</a>" : <i>String</i>,
        "<a href="#b64std" title="B64Std">B64Std</a>" : <i>String</i>,
        "<a href="#b64url" title="B64Url">B64Url</a>" : <i>String</i>,
        "<a href="#bytelength" title="ByteLength">ByteLength</a>" : <i>Double</i>,
        "<a href="#dec" title="Dec">Dec</a>" : <i>String</i>,
        "<a href="#hex" title="Hex">Hex</a>" : <i>String</i>,
        "<a href="#keepers" title="Keepers">Keepers</a>" : <i>[ &lt;a href=&#34;keepers.md&#34;&gt;Keepers&lt;/a&gt;, ... ]</i>,
        "<a href="#prefix" title="Prefix">Prefix</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Random::Id
Properties:
    <a href="#tfcfnid" title="tfcfnid">tfcfnid</a>: <i>String</i>
    <a href="#b64" title="B64">B64</a>: <i>String</i>
    <a href="#b64std" title="B64Std">B64Std</a>: <i>String</i>
    <a href="#b64url" title="B64Url">B64Url</a>: <i>String</i>
    <a href="#bytelength" title="ByteLength">ByteLength</a>: <i>Double</i>
    <a href="#dec" title="Dec">Dec</a>: <i>String</i>
    <a href="#hex" title="Hex">Hex</a>: <i>String</i>
    <a href="#keepers" title="Keepers">Keepers</a>: <i>
      - &lt;a href=&#34;keepers.md&#34;&gt;Keepers&lt;/a&gt;</i>
    <a href="#prefix" title="Prefix">Prefix</a>: <i>String</i>
</pre>

## Properties

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### B64

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### B64Std

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### B64Url

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ByteLength

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Dec

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Hex

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Keepers

_Required_: No

_Type_: List of &lt;a href=&#34;keepers.md&#34;&gt;Keepers&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Prefix

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

#### B64

Returns the &lt;code&gt;B64&lt;/code&gt; value.

#### B64Std

Returns the &lt;code&gt;B64Std&lt;/code&gt; value.

#### B64Url

Returns the &lt;code&gt;B64Url&lt;/code&gt; value.

#### Dec

Returns the &lt;code&gt;Dec&lt;/code&gt; value.

#### Hex

Returns the &lt;code&gt;Hex&lt;/code&gt; value.

