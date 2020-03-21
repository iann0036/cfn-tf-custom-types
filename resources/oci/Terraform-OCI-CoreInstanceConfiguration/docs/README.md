# Terraform::OCI::CoreInstanceConfiguration

CloudFormation equivalent of oci_core_instance_configuration

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::OCI::CoreInstanceConfiguration",
    "Properties" : {
        "<a href="#tfcfnid" title="tfcfnid">tfcfnid</a>" : <i>String</i>,
        "<a href="#compartmentid" title="CompartmentId">CompartmentId</a>" : <i>String</i>,
        "<a href="#deferredfields" title="DeferredFields">DeferredFields</a>" : <i>[ String, ... ]</i>,
        "<a href="#definedtags" title="DefinedTags">DefinedTags</a>" : <i>[ &lt;a href=&#34;definedtags.md&#34;&gt;DefinedTags&lt;/a&gt;, ... ]</i>,
        "<a href="#displayname" title="DisplayName">DisplayName</a>" : <i>String</i>,
        "<a href="#freeformtags" title="FreeformTags">FreeformTags</a>" : <i>[ &lt;a href=&#34;freeformtags.md&#34;&gt;FreeformTags&lt;/a&gt;, ... ]</i>,
        "<a href="#instanceid" title="InstanceId">InstanceId</a>" : <i>String</i>,
        "<a href="#source" title="Source">Source</a>" : <i>String</i>,
        "<a href="#timecreated" title="TimeCreated">TimeCreated</a>" : <i>String</i>,
        "<a href="#instancedetails" title="InstanceDetails">InstanceDetails</a>" : <i>[ &lt;a href=&#34;instancedetails.md&#34;&gt;InstanceDetails&lt;/a&gt;, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i>&lt;a href=&#34;timeouts.md&#34;&gt;Timeouts&lt;/a&gt;</i>,
        "<a href="#blockvolumes" title="BlockVolumes">BlockVolumes</a>" : <i>[ &lt;a href=&#34;blockvolumes.md&#34;&gt;BlockVolumes&lt;/a&gt;, ... ]</i>,
        "<a href="#launchdetails" title="LaunchDetails">LaunchDetails</a>" : <i>[ &lt;a href=&#34;launchdetails.md&#34;&gt;LaunchDetails&lt;/a&gt;, ... ]</i>,
        "<a href="#secondaryvnics" title="SecondaryVnics">SecondaryVnics</a>" : <i>[ &lt;a href=&#34;secondaryvnics.md&#34;&gt;SecondaryVnics&lt;/a&gt;, ... ]</i>,
        "<a href="#attachdetails" title="AttachDetails">AttachDetails</a>" : <i>[ &lt;a href=&#34;attachdetails.md&#34;&gt;AttachDetails&lt;/a&gt;, ... ]</i>,
        "<a href="#createdetails" title="CreateDetails">CreateDetails</a>" : <i>[ &lt;a href=&#34;createdetails.md&#34;&gt;CreateDetails&lt;/a&gt;, ... ]</i>,
        "<a href="#createvnicdetails" title="CreateVnicDetails">CreateVnicDetails</a>" : <i>[ &lt;a href=&#34;createvnicdetails.md&#34;&gt;CreateVnicDetails&lt;/a&gt;, ... ]</i>,
        "<a href="#sourcedetails" title="SourceDetails">SourceDetails</a>" : <i>[ &lt;a href=&#34;sourcedetails.md&#34;&gt;SourceDetails&lt;/a&gt;, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::OCI::CoreInstanceConfiguration
Properties:
    <a href="#tfcfnid" title="tfcfnid">tfcfnid</a>: <i>String</i>
    <a href="#compartmentid" title="CompartmentId">CompartmentId</a>: <i>String</i>
    <a href="#deferredfields" title="DeferredFields">DeferredFields</a>: <i>
      - String</i>
    <a href="#definedtags" title="DefinedTags">DefinedTags</a>: <i>
      - &lt;a href=&#34;definedtags.md&#34;&gt;DefinedTags&lt;/a&gt;</i>
    <a href="#displayname" title="DisplayName">DisplayName</a>: <i>String</i>
    <a href="#freeformtags" title="FreeformTags">FreeformTags</a>: <i>
      - &lt;a href=&#34;freeformtags.md&#34;&gt;FreeformTags&lt;/a&gt;</i>
    <a href="#instanceid" title="InstanceId">InstanceId</a>: <i>String</i>
    <a href="#source" title="Source">Source</a>: <i>String</i>
    <a href="#timecreated" title="TimeCreated">TimeCreated</a>: <i>String</i>
    <a href="#instancedetails" title="InstanceDetails">InstanceDetails</a>: <i>
      - &lt;a href=&#34;instancedetails.md&#34;&gt;InstanceDetails&lt;/a&gt;</i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i>&lt;a href=&#34;timeouts.md&#34;&gt;Timeouts&lt;/a&gt;</i>
    <a href="#blockvolumes" title="BlockVolumes">BlockVolumes</a>: <i>
      - &lt;a href=&#34;blockvolumes.md&#34;&gt;BlockVolumes&lt;/a&gt;</i>
    <a href="#launchdetails" title="LaunchDetails">LaunchDetails</a>: <i>
      - &lt;a href=&#34;launchdetails.md&#34;&gt;LaunchDetails&lt;/a&gt;</i>
    <a href="#secondaryvnics" title="SecondaryVnics">SecondaryVnics</a>: <i>
      - &lt;a href=&#34;secondaryvnics.md&#34;&gt;SecondaryVnics&lt;/a&gt;</i>
    <a href="#attachdetails" title="AttachDetails">AttachDetails</a>: <i>
      - &lt;a href=&#34;attachdetails.md&#34;&gt;AttachDetails&lt;/a&gt;</i>
    <a href="#createdetails" title="CreateDetails">CreateDetails</a>: <i>
      - &lt;a href=&#34;createdetails.md&#34;&gt;CreateDetails&lt;/a&gt;</i>
    <a href="#createvnicdetails" title="CreateVnicDetails">CreateVnicDetails</a>: <i>
      - &lt;a href=&#34;createvnicdetails.md&#34;&gt;CreateVnicDetails&lt;/a&gt;</i>
    <a href="#sourcedetails" title="SourceDetails">SourceDetails</a>: <i>
      - &lt;a href=&#34;sourcedetails.md&#34;&gt;SourceDetails&lt;/a&gt;</i>
</pre>

## Properties

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CompartmentId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DeferredFields

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefinedTags

_Required_: No

_Type_: List of &lt;a href=&#34;definedtags.md&#34;&gt;DefinedTags&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisplayName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FreeformTags

_Required_: No

_Type_: List of &lt;a href=&#34;freeformtags.md&#34;&gt;FreeformTags&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InstanceId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Source

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TimeCreated

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InstanceDetails

_Required_: No

_Type_: List of &lt;a href=&#34;instancedetails.md&#34;&gt;InstanceDetails&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: &lt;a href=&#34;timeouts.md&#34;&gt;Timeouts&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BlockVolumes

_Required_: No

_Type_: List of &lt;a href=&#34;blockvolumes.md&#34;&gt;BlockVolumes&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LaunchDetails

_Required_: No

_Type_: List of &lt;a href=&#34;launchdetails.md&#34;&gt;LaunchDetails&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecondaryVnics

_Required_: No

_Type_: List of &lt;a href=&#34;secondaryvnics.md&#34;&gt;SecondaryVnics&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AttachDetails

_Required_: No

_Type_: List of &lt;a href=&#34;attachdetails.md&#34;&gt;AttachDetails&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CreateDetails

_Required_: No

_Type_: List of &lt;a href=&#34;createdetails.md&#34;&gt;CreateDetails&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CreateVnicDetails

_Required_: No

_Type_: List of &lt;a href=&#34;createvnicdetails.md&#34;&gt;CreateVnicDetails&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceDetails

_Required_: No

_Type_: List of &lt;a href=&#34;sourcedetails.md&#34;&gt;SourceDetails&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### DeferredFields

Returns the &lt;code&gt;DeferredFields&lt;/code&gt; value.

#### TimeCreated

Returns the &lt;code&gt;TimeCreated&lt;/code&gt; value.

