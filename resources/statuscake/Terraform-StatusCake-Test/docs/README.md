# Terraform::StatusCake::Test

CloudFormation equivalent of statuscake_test

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::StatusCake::Test",
    "Properties" : {
        "<a href="#tfcfnid" title="tfcfnid">tfcfnid</a>" : <i>String</i>,
        "<a href="#basicpass" title="BasicPass">BasicPass</a>" : <i>String</i>,
        "<a href="#basicuser" title="BasicUser">BasicUser</a>" : <i>String</i>,
        "<a href="#branding" title="Branding">Branding</a>" : <i>Double</i>,
        "<a href="#checkrate" title="CheckRate">CheckRate</a>" : <i>Double</i>,
        "<a href="#confirmations" title="Confirmations">Confirmations</a>" : <i>Double</i>,
        "<a href="#contactgroup" title="ContactGroup">ContactGroup</a>" : <i>[ String, ... ]</i>,
        "<a href="#contactid" title="ContactId">ContactId</a>" : <i>Double</i>,
        "<a href="#customheader" title="CustomHeader">CustomHeader</a>" : <i>String</i>,
        "<a href="#donotfind" title="DoNotFind">DoNotFind</a>" : <i>Boolean</i>,
        "<a href="#enablesslalert" title="EnableSslAlert">EnableSslAlert</a>" : <i>Boolean</i>,
        "<a href="#finalendpoint" title="FinalEndpoint">FinalEndpoint</a>" : <i>String</i>,
        "<a href="#findstring" title="FindString">FindString</a>" : <i>String</i>,
        "<a href="#followredirect" title="FollowRedirect">FollowRedirect</a>" : <i>Boolean</i>,
        "<a href="#logoimage" title="LogoImage">LogoImage</a>" : <i>String</i>,
        "<a href="#nodelocations" title="NodeLocations">NodeLocations</a>" : <i>[ String, ... ]</i>,
        "<a href="#paused" title="Paused">Paused</a>" : <i>Boolean</i>,
        "<a href="#pingurl" title="PingUrl">PingUrl</a>" : <i>String</i>,
        "<a href="#port" title="Port">Port</a>" : <i>Double</i>,
        "<a href="#postraw" title="PostRaw">PostRaw</a>" : <i>String</i>,
        "<a href="#public" title="Public">Public</a>" : <i>Double</i>,
        "<a href="#realbrowser" title="RealBrowser">RealBrowser</a>" : <i>Double</i>,
        "<a href="#status" title="Status">Status</a>" : <i>String</i>,
        "<a href="#statuscodes" title="StatusCodes">StatusCodes</a>" : <i>String</i>,
        "<a href="#testid" title="TestId">TestId</a>" : <i>String</i>,
        "<a href="#testtags" title="TestTags">TestTags</a>" : <i>[ String, ... ]</i>,
        "<a href="#testtype" title="TestType">TestType</a>" : <i>String</i>,
        "<a href="#timeout" title="Timeout">Timeout</a>" : <i>Double</i>,
        "<a href="#triggerrate" title="TriggerRate">TriggerRate</a>" : <i>Double</i>,
        "<a href="#uptime" title="Uptime">Uptime</a>" : <i>Double</i>,
        "<a href="#usejar" title="UseJar">UseJar</a>" : <i>Double</i>,
        "<a href="#useragent" title="UserAgent">UserAgent</a>" : <i>String</i>,
        "<a href="#virus" title="Virus">Virus</a>" : <i>Double</i>,
        "<a href="#websitehost" title="WebsiteHost">WebsiteHost</a>" : <i>String</i>,
        "<a href="#websitename" title="WebsiteName">WebsiteName</a>" : <i>String</i>,
        "<a href="#websiteurl" title="WebsiteUrl">WebsiteUrl</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::StatusCake::Test
Properties:
    <a href="#tfcfnid" title="tfcfnid">tfcfnid</a>: <i>String</i>
    <a href="#basicpass" title="BasicPass">BasicPass</a>: <i>String</i>
    <a href="#basicuser" title="BasicUser">BasicUser</a>: <i>String</i>
    <a href="#branding" title="Branding">Branding</a>: <i>Double</i>
    <a href="#checkrate" title="CheckRate">CheckRate</a>: <i>Double</i>
    <a href="#confirmations" title="Confirmations">Confirmations</a>: <i>Double</i>
    <a href="#contactgroup" title="ContactGroup">ContactGroup</a>: <i>
      - String</i>
    <a href="#contactid" title="ContactId">ContactId</a>: <i>Double</i>
    <a href="#customheader" title="CustomHeader">CustomHeader</a>: <i>String</i>
    <a href="#donotfind" title="DoNotFind">DoNotFind</a>: <i>Boolean</i>
    <a href="#enablesslalert" title="EnableSslAlert">EnableSslAlert</a>: <i>Boolean</i>
    <a href="#finalendpoint" title="FinalEndpoint">FinalEndpoint</a>: <i>String</i>
    <a href="#findstring" title="FindString">FindString</a>: <i>String</i>
    <a href="#followredirect" title="FollowRedirect">FollowRedirect</a>: <i>Boolean</i>
    <a href="#logoimage" title="LogoImage">LogoImage</a>: <i>String</i>
    <a href="#nodelocations" title="NodeLocations">NodeLocations</a>: <i>
      - String</i>
    <a href="#paused" title="Paused">Paused</a>: <i>Boolean</i>
    <a href="#pingurl" title="PingUrl">PingUrl</a>: <i>String</i>
    <a href="#port" title="Port">Port</a>: <i>Double</i>
    <a href="#postraw" title="PostRaw">PostRaw</a>: <i>String</i>
    <a href="#public" title="Public">Public</a>: <i>Double</i>
    <a href="#realbrowser" title="RealBrowser">RealBrowser</a>: <i>Double</i>
    <a href="#status" title="Status">Status</a>: <i>String</i>
    <a href="#statuscodes" title="StatusCodes">StatusCodes</a>: <i>String</i>
    <a href="#testid" title="TestId">TestId</a>: <i>String</i>
    <a href="#testtags" title="TestTags">TestTags</a>: <i>
      - String</i>
    <a href="#testtype" title="TestType">TestType</a>: <i>String</i>
    <a href="#timeout" title="Timeout">Timeout</a>: <i>Double</i>
    <a href="#triggerrate" title="TriggerRate">TriggerRate</a>: <i>Double</i>
    <a href="#uptime" title="Uptime">Uptime</a>: <i>Double</i>
    <a href="#usejar" title="UseJar">UseJar</a>: <i>Double</i>
    <a href="#useragent" title="UserAgent">UserAgent</a>: <i>String</i>
    <a href="#virus" title="Virus">Virus</a>: <i>Double</i>
    <a href="#websitehost" title="WebsiteHost">WebsiteHost</a>: <i>String</i>
    <a href="#websitename" title="WebsiteName">WebsiteName</a>: <i>String</i>
    <a href="#websiteurl" title="WebsiteUrl">WebsiteUrl</a>: <i>String</i>
</pre>

## Properties

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BasicPass

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BasicUser

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Branding

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CheckRate

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Confirmations

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ContactGroup

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ContactId

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CustomHeader

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DoNotFind

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableSslAlert

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FinalEndpoint

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FindString

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FollowRedirect

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LogoImage

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NodeLocations

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Paused

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PingUrl

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Port

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PostRaw

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Public

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RealBrowser

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Status

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StatusCodes

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TestId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TestTags

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TestType

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeout

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TriggerRate

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Uptime

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UseJar

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UserAgent

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Virus

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WebsiteHost

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WebsiteName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WebsiteUrl

_Required_: Yes

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

#### Status

Returns the &lt;code&gt;Status&lt;/code&gt; value.

#### TestId

Returns the &lt;code&gt;TestId&lt;/code&gt; value.

#### Uptime

Returns the &lt;code&gt;Uptime&lt;/code&gt; value.

