# TF::AVI::Applicationprofile RlProfileDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#clientipconnectionsratelimit" title="ClientIpConnectionsRateLimit">ClientIpConnectionsRateLimit</a>" : <i>[ <a href="clientipconnectionsratelimitdefinition.md">ClientIpConnectionsRateLimitDefinition</a>, ... ]</i>,
    "<a href="#clientipfailedrequestsratelimit" title="ClientIpFailedRequestsRateLimit">ClientIpFailedRequestsRateLimit</a>" : <i>[ <a href="clientipfailedrequestsratelimitdefinition.md">ClientIpFailedRequestsRateLimitDefinition</a>, ... ]</i>,
    "<a href="#clientiprequestsratelimit" title="ClientIpRequestsRateLimit">ClientIpRequestsRateLimit</a>" : <i>[ <a href="clientiprequestsratelimitdefinition.md">ClientIpRequestsRateLimitDefinition</a>, ... ]</i>,
    "<a href="#clientipscannersrequestsratelimit" title="ClientIpScannersRequestsRateLimit">ClientIpScannersRequestsRateLimit</a>" : <i>[ <a href="clientipscannersrequestsratelimitdefinition.md">ClientIpScannersRequestsRateLimitDefinition</a>, ... ]</i>,
    "<a href="#clientiptourifailedrequestsratelimit" title="ClientIpToUriFailedRequestsRateLimit">ClientIpToUriFailedRequestsRateLimit</a>" : <i>[ <a href="clientiptourifailedrequestsratelimitdefinition.md">ClientIpToUriFailedRequestsRateLimitDefinition</a>, ... ]</i>,
    "<a href="#clientiptourirequestsratelimit" title="ClientIpToUriRequestsRateLimit">ClientIpToUriRequestsRateLimit</a>" : <i>[ <a href="clientiptourirequestsratelimitdefinition.md">ClientIpToUriRequestsRateLimitDefinition</a>, ... ]</i>,
    "<a href="#customrequestsratelimit" title="CustomRequestsRateLimit">CustomRequestsRateLimit</a>" : <i>[ <a href="customrequestsratelimitdefinition.md">CustomRequestsRateLimitDefinition</a>, ... ]</i>,
    "<a href="#httpheaderratelimits" title="HttpHeaderRateLimits">HttpHeaderRateLimits</a>" : <i>[ <a href="httpheaderratelimitsdefinition.md">HttpHeaderRateLimitsDefinition</a>, ... ]</i>,
    "<a href="#urifailedrequestsratelimit" title="UriFailedRequestsRateLimit">UriFailedRequestsRateLimit</a>" : <i>[ <a href="urifailedrequestsratelimitdefinition.md">UriFailedRequestsRateLimitDefinition</a>, ... ]</i>,
    "<a href="#urirequestsratelimit" title="UriRequestsRateLimit">UriRequestsRateLimit</a>" : <i>[ <a href="urirequestsratelimitdefinition.md">UriRequestsRateLimitDefinition</a>, ... ]</i>,
    "<a href="#uriscannersrequestsratelimit" title="UriScannersRequestsRateLimit">UriScannersRequestsRateLimit</a>" : <i>[ <a href="uriscannersrequestsratelimitdefinition.md">UriScannersRequestsRateLimitDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#clientipconnectionsratelimit" title="ClientIpConnectionsRateLimit">ClientIpConnectionsRateLimit</a>: <i>
      - <a href="clientipconnectionsratelimitdefinition.md">ClientIpConnectionsRateLimitDefinition</a></i>
<a href="#clientipfailedrequestsratelimit" title="ClientIpFailedRequestsRateLimit">ClientIpFailedRequestsRateLimit</a>: <i>
      - <a href="clientipfailedrequestsratelimitdefinition.md">ClientIpFailedRequestsRateLimitDefinition</a></i>
<a href="#clientiprequestsratelimit" title="ClientIpRequestsRateLimit">ClientIpRequestsRateLimit</a>: <i>
      - <a href="clientiprequestsratelimitdefinition.md">ClientIpRequestsRateLimitDefinition</a></i>
<a href="#clientipscannersrequestsratelimit" title="ClientIpScannersRequestsRateLimit">ClientIpScannersRequestsRateLimit</a>: <i>
      - <a href="clientipscannersrequestsratelimitdefinition.md">ClientIpScannersRequestsRateLimitDefinition</a></i>
<a href="#clientiptourifailedrequestsratelimit" title="ClientIpToUriFailedRequestsRateLimit">ClientIpToUriFailedRequestsRateLimit</a>: <i>
      - <a href="clientiptourifailedrequestsratelimitdefinition.md">ClientIpToUriFailedRequestsRateLimitDefinition</a></i>
<a href="#clientiptourirequestsratelimit" title="ClientIpToUriRequestsRateLimit">ClientIpToUriRequestsRateLimit</a>: <i>
      - <a href="clientiptourirequestsratelimitdefinition.md">ClientIpToUriRequestsRateLimitDefinition</a></i>
<a href="#customrequestsratelimit" title="CustomRequestsRateLimit">CustomRequestsRateLimit</a>: <i>
      - <a href="customrequestsratelimitdefinition.md">CustomRequestsRateLimitDefinition</a></i>
<a href="#httpheaderratelimits" title="HttpHeaderRateLimits">HttpHeaderRateLimits</a>: <i>
      - <a href="httpheaderratelimitsdefinition.md">HttpHeaderRateLimitsDefinition</a></i>
<a href="#urifailedrequestsratelimit" title="UriFailedRequestsRateLimit">UriFailedRequestsRateLimit</a>: <i>
      - <a href="urifailedrequestsratelimitdefinition.md">UriFailedRequestsRateLimitDefinition</a></i>
<a href="#urirequestsratelimit" title="UriRequestsRateLimit">UriRequestsRateLimit</a>: <i>
      - <a href="urirequestsratelimitdefinition.md">UriRequestsRateLimitDefinition</a></i>
<a href="#uriscannersrequestsratelimit" title="UriScannersRequestsRateLimit">UriScannersRequestsRateLimit</a>: <i>
      - <a href="uriscannersrequestsratelimitdefinition.md">UriScannersRequestsRateLimitDefinition</a></i>
</pre>

## Properties

#### ClientIpConnectionsRateLimit

_Required_: No

_Type_: List of <a href="clientipconnectionsratelimitdefinition.md">ClientIpConnectionsRateLimitDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClientIpFailedRequestsRateLimit

_Required_: No

_Type_: List of <a href="clientipfailedrequestsratelimitdefinition.md">ClientIpFailedRequestsRateLimitDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClientIpRequestsRateLimit

_Required_: No

_Type_: List of <a href="clientiprequestsratelimitdefinition.md">ClientIpRequestsRateLimitDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClientIpScannersRequestsRateLimit

_Required_: No

_Type_: List of <a href="clientipscannersrequestsratelimitdefinition.md">ClientIpScannersRequestsRateLimitDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClientIpToUriFailedRequestsRateLimit

_Required_: No

_Type_: List of <a href="clientiptourifailedrequestsratelimitdefinition.md">ClientIpToUriFailedRequestsRateLimitDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClientIpToUriRequestsRateLimit

_Required_: No

_Type_: List of <a href="clientiptourirequestsratelimitdefinition.md">ClientIpToUriRequestsRateLimitDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CustomRequestsRateLimit

_Required_: No

_Type_: List of <a href="customrequestsratelimitdefinition.md">CustomRequestsRateLimitDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HttpHeaderRateLimits

_Required_: No

_Type_: List of <a href="httpheaderratelimitsdefinition.md">HttpHeaderRateLimitsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UriFailedRequestsRateLimit

_Required_: No

_Type_: List of <a href="urifailedrequestsratelimitdefinition.md">UriFailedRequestsRateLimitDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UriRequestsRateLimit

_Required_: No

_Type_: List of <a href="urirequestsratelimitdefinition.md">UriRequestsRateLimitDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UriScannersRequestsRateLimit

_Required_: No

_Type_: List of <a href="uriscannersrequestsratelimitdefinition.md">UriScannersRequestsRateLimitDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

