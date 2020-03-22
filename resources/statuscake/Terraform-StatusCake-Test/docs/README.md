# Terraform::StatusCake::Test

The test resource allows StatusCake tests to be managed by Terraform.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::StatusCake::Test",
    "Properties" : {
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
        "<a href="#statuscodes" title="StatusCodes">StatusCodes</a>" : <i>String</i>,
        "<a href="#testtags" title="TestTags">TestTags</a>" : <i>[ String, ... ]</i>,
        "<a href="#testtype" title="TestType">TestType</a>" : <i>String</i>,
        "<a href="#timeout" title="Timeout">Timeout</a>" : <i>Double</i>,
        "<a href="#triggerrate" title="TriggerRate">TriggerRate</a>" : <i>Double</i>,
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
    <a href="#statuscodes" title="StatusCodes">StatusCodes</a>: <i>String</i>
    <a href="#testtags" title="TestTags">TestTags</a>: <i>
      - String</i>
    <a href="#testtype" title="TestType">TestType</a>: <i>String</i>
    <a href="#timeout" title="Timeout">Timeout</a>: <i>Double</i>
    <a href="#triggerrate" title="TriggerRate">TriggerRate</a>: <i>Double</i>
    <a href="#usejar" title="UseJar">UseJar</a>: <i>Double</i>
    <a href="#useragent" title="UserAgent">UserAgent</a>: <i>String</i>
    <a href="#virus" title="Virus">Virus</a>: <i>Double</i>
    <a href="#websitehost" title="WebsiteHost">WebsiteHost</a>: <i>String</i>
    <a href="#websitename" title="WebsiteName">WebsiteName</a>: <i>String</i>
    <a href="#websiteurl" title="WebsiteUrl">WebsiteUrl</a>: <i>String</i>
</pre>

## Properties

#### BasicPass

If BasicUser is set then this should be the password for the BasicUser.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BasicUser

A Basic Auth User account to use to login.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Branding

Set to 0 to use branding (default) or 1 to disable public reporting branding).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CheckRate

Test check rate in seconds. Defaults to 300.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Confirmations

The number of confirmation servers to use in order to detect downtime. Defaults to 0.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ContactGroup

Set test contact groups, must be array of strings.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ContactId

**Deprecated** (Optional) The id of the contact group to be added to the test. Each test can have only one.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CustomHeader

Custom HTTP header, must be supplied as JSON.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DoNotFind

If the above string should be found to trigger a alert. 1 = will trigger if find_string found.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableSslAlert

HTTP Tests only. If enabled, tests will send warnings if the SSL certificate is about to expire. Paid users only. Default is false.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FinalEndpoint

Use to specify the expected Final URL in the testing process.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FindString

A string that should either be found or not found.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FollowRedirect

Use to specify whether redirects should be followed, set to true to enable. Default is false.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LogoImage

A URL to a image to use for public reporting.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NodeLocations

Set test node locations, must be array of strings.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Paused

Whether or not the test is paused. Defaults to false.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PingUrl

A URL to ping if a site goes down.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Port

The port to use when specifying a TCP test.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PostRaw

Use to populate the RAW POST data field on the test.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Public

Set 1 to enable public reporting, 0 to disable.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RealBrowser

Use 1 to TURN OFF real browser testing.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StatusCodes

Comma Separated List of StatusCodes to Trigger Error on. Defaults are "204, 205, 206, 303, 400, 401, 403, 404, 405, 406, 408, 410, 413, 444, 429, 494, 495, 496, 499, 500, 501, 502, 503, 504, 505, 506, 507, 508, 509, 510, 511, 521, 522, 523, 524, 520, 598, 599".

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TestTags

Set test tags, must be array of strings.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TestType

The type of Test. Either HTTP, TCP, PING, or DNS.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeout

The timeout of the test in seconds.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TriggerRate

The number of minutes to wait before sending an alert. Default is `5`.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UseJar

Set to true to enable the Cookie Jar. Required for some redirects. Default is false.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UserAgent

Test with a custom user agent set.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Virus

Enable virus checking or not. 1 to enable.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WebsiteHost

Used internally, when possible please add.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WebsiteName

This is the name of the test and the website to be monitored.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WebsiteUrl

The URL of the website to be monitored.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the Id.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Id

Returns the <code>Id</code> value.

#### Status

Returns the <code>Status</code> value.

#### TestId

Returns the <code>TestId</code> value.

#### Uptime

Returns the <code>Uptime</code> value.

