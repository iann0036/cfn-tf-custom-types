# TF::AVI::Healthmonitor HttpMonitorDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#authtype" title="AuthType">AuthType</a>" : <i>String</i>,
    "<a href="#exacthttprequest" title="ExactHttpRequest">ExactHttpRequest</a>" : <i>Boolean</i>,
    "<a href="#httprequest" title="HttpRequest">HttpRequest</a>" : <i>String</i>,
    "<a href="#httprequestbody" title="HttpRequestBody">HttpRequestBody</a>" : <i>String</i>,
    "<a href="#httpresponse" title="HttpResponse">HttpResponse</a>" : <i>String</i>,
    "<a href="#httpresponsecode" title="HttpResponseCode">HttpResponseCode</a>" : <i>[ String, ... ]</i>,
    "<a href="#maintenancecode" title="MaintenanceCode">MaintenanceCode</a>" : <i>[ Double, ... ]</i>,
    "<a href="#maintenanceresponse" title="MaintenanceResponse">MaintenanceResponse</a>" : <i>String</i>,
    "<a href="#responsesize" title="ResponseSize">ResponseSize</a>" : <i>Double</i>,
    "<a href="#sslattributes" title="SslAttributes">SslAttributes</a>" : <i>[ <a href="sslattributesdefinition.md">SslAttributesDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#authtype" title="AuthType">AuthType</a>: <i>String</i>
<a href="#exacthttprequest" title="ExactHttpRequest">ExactHttpRequest</a>: <i>Boolean</i>
<a href="#httprequest" title="HttpRequest">HttpRequest</a>: <i>String</i>
<a href="#httprequestbody" title="HttpRequestBody">HttpRequestBody</a>: <i>String</i>
<a href="#httpresponse" title="HttpResponse">HttpResponse</a>: <i>String</i>
<a href="#httpresponsecode" title="HttpResponseCode">HttpResponseCode</a>: <i>
      - String</i>
<a href="#maintenancecode" title="MaintenanceCode">MaintenanceCode</a>: <i>
      - Double</i>
<a href="#maintenanceresponse" title="MaintenanceResponse">MaintenanceResponse</a>: <i>String</i>
<a href="#responsesize" title="ResponseSize">ResponseSize</a>: <i>Double</i>
<a href="#sslattributes" title="SslAttributes">SslAttributes</a>: <i>
      - <a href="sslattributesdefinition.md">SslAttributesDefinition</a></i>
</pre>

## Properties

#### AuthType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExactHttpRequest

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HttpRequest

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HttpRequestBody

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HttpResponse

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HttpResponseCode

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaintenanceCode

_Required_: No

_Type_: List of Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaintenanceResponse

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResponseSize

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SslAttributes

_Required_: No

_Type_: List of <a href="sslattributesdefinition.md">SslAttributesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

