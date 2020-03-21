# Terraform::Heroku::Build

CloudFormation equivalent of heroku_build

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Heroku::Build",
    "Properties" : {
        "<a href="#tfcfnid" title="tfcfnid">tfcfnid</a>" : <i>String</i>,
        "<a href="#app" title="App">App</a>" : <i>String</i>,
        "<a href="#buildpacks" title="Buildpacks">Buildpacks</a>" : <i>[ String, ... ]</i>,
        "<a href="#localchecksum" title="LocalChecksum">LocalChecksum</a>" : <i>String</i>,
        "<a href="#outputstreamurl" title="OutputStreamUrl">OutputStreamUrl</a>" : <i>String</i>,
        "<a href="#releaseid" title="ReleaseId">ReleaseId</a>" : <i>String</i>,
        "<a href="#slugid" title="SlugId">SlugId</a>" : <i>String</i>,
        "<a href="#source" title="Source">Source</a>" : <i>[ &lt;a href=&#34;source.md&#34;&gt;Source&lt;/a&gt;, ... ]</i>,
        "<a href="#stack" title="Stack">Stack</a>" : <i>String</i>,
        "<a href="#status" title="Status">Status</a>" : <i>String</i>,
        "<a href="#user" title="User">User</a>" : <i>[ &lt;a href=&#34;user.md&#34;&gt;User&lt;/a&gt;, ... ]</i>,
        "<a href="#uuid" title="Uuid">Uuid</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Heroku::Build
Properties:
    <a href="#tfcfnid" title="tfcfnid">tfcfnid</a>: <i>String</i>
    <a href="#app" title="App">App</a>: <i>String</i>
    <a href="#buildpacks" title="Buildpacks">Buildpacks</a>: <i>
      - String</i>
    <a href="#localchecksum" title="LocalChecksum">LocalChecksum</a>: <i>String</i>
    <a href="#outputstreamurl" title="OutputStreamUrl">OutputStreamUrl</a>: <i>String</i>
    <a href="#releaseid" title="ReleaseId">ReleaseId</a>: <i>String</i>
    <a href="#slugid" title="SlugId">SlugId</a>: <i>String</i>
    <a href="#source" title="Source">Source</a>: <i>
      - &lt;a href=&#34;source.md&#34;&gt;Source&lt;/a&gt;</i>
    <a href="#stack" title="Stack">Stack</a>: <i>String</i>
    <a href="#status" title="Status">Status</a>: <i>String</i>
    <a href="#user" title="User">User</a>: <i>
      - &lt;a href=&#34;user.md&#34;&gt;User&lt;/a&gt;</i>
    <a href="#uuid" title="Uuid">Uuid</a>: <i>String</i>
</pre>

## Properties

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### App

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Buildpacks

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LocalChecksum

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OutputStreamUrl

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ReleaseId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SlugId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Source

_Required_: Yes

_Type_: List of &lt;a href=&#34;source.md&#34;&gt;Source&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Stack

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Status

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### User

_Required_: No

_Type_: List of &lt;a href=&#34;user.md&#34;&gt;User&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Uuid

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

#### LocalChecksum

Returns the &lt;code&gt;LocalChecksum&lt;/code&gt; value.

#### OutputStreamUrl

Returns the &lt;code&gt;OutputStreamUrl&lt;/code&gt; value.

#### ReleaseId

Returns the &lt;code&gt;ReleaseId&lt;/code&gt; value.

#### SlugId

Returns the &lt;code&gt;SlugId&lt;/code&gt; value.

#### Stack

Returns the &lt;code&gt;Stack&lt;/code&gt; value.

#### Status

Returns the &lt;code&gt;Status&lt;/code&gt; value.

#### User

Returns the &lt;code&gt;User&lt;/code&gt; value.

#### Uuid

Returns the &lt;code&gt;Uuid&lt;/code&gt; value.

