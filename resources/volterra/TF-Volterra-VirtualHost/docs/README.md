# TF::Volterra::VirtualHost

CloudFormation equivalent of volterra_virtual_host

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Volterra::VirtualHost",
    "Properties" : {
        "<a href="#addlocation" title="AddLocation">AddLocation</a>" : <i>Boolean</i>,
        "<a href="#annotations" title="Annotations">Annotations</a>" : <i>[ <a href="annotationsdefinition.md">AnnotationsDefinition</a>, ... ]</i>,
        "<a href="#appendservername" title="AppendServerName">AppendServerName</a>" : <i>String</i>,
        "<a href="#customerrors" title="CustomErrors">CustomErrors</a>" : <i>[ <a href="customerrorsdefinition.md">CustomErrorsDefinition</a>, ... ]</i>,
        "<a href="#defaultheader" title="DefaultHeader">DefaultHeader</a>" : <i>Boolean</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#disable" title="Disable">Disable</a>" : <i>Boolean</i>,
        "<a href="#disabledefaulterrorpages" title="DisableDefaultErrorPages">DisableDefaultErrorPages</a>" : <i>Boolean</i>,
        "<a href="#disablednsresolve" title="DisableDnsResolve">DisableDnsResolve</a>" : <i>Boolean</i>,
        "<a href="#domains" title="Domains">Domains</a>" : <i>[ String, ... ]</i>,
        "<a href="#idletimeout" title="IdleTimeout">IdleTimeout</a>" : <i>Double</i>,
        "<a href="#labels" title="Labels">Labels</a>" : <i>[ <a href="labelsdefinition.md">LabelsDefinition</a>, ... ]</i>,
        "<a href="#maxrequestheadersize" title="MaxRequestHeaderSize">MaxRequestHeaderSize</a>" : <i>Double</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#namespace" title="Namespace">Namespace</a>" : <i>String</i>,
        "<a href="#noauthentication" title="NoAuthentication">NoAuthentication</a>" : <i>Boolean</i>,
        "<a href="#nochallenge" title="NoChallenge">NoChallenge</a>" : <i>Boolean</i>,
        "<a href="#passthrough" title="PassThrough">PassThrough</a>" : <i>Boolean</i>,
        "<a href="#proxy" title="Proxy">Proxy</a>" : <i>String</i>,
        "<a href="#requestheaderstoremove" title="RequestHeadersToRemove">RequestHeadersToRemove</a>" : <i>[ String, ... ]</i>,
        "<a href="#responseheaderstoremove" title="ResponseHeadersToRemove">ResponseHeadersToRemove</a>" : <i>[ String, ... ]</i>,
        "<a href="#servername" title="ServerName">ServerName</a>" : <i>String</i>,
        "<a href="#advertisepolicies" title="AdvertisePolicies">AdvertisePolicies</a>" : <i>[ <a href="advertisepoliciesdefinition.md">AdvertisePoliciesDefinition</a>, ... ]</i>,
        "<a href="#authentication" title="Authentication">Authentication</a>" : <i>[ <a href="authenticationdefinition.md">AuthenticationDefinition</a>, ... ]</i>,
        "<a href="#bufferpolicy" title="BufferPolicy">BufferPolicy</a>" : <i>[ <a href="bufferpolicydefinition.md">BufferPolicyDefinition</a>, ... ]</i>,
        "<a href="#captchachallenge" title="CaptchaChallenge">CaptchaChallenge</a>" : <i>[ <a href="captchachallengedefinition.md">CaptchaChallengeDefinition</a>, ... ]</i>,
        "<a href="#compressionparams" title="CompressionParams">CompressionParams</a>" : <i>[ <a href="compressionparamsdefinition.md">CompressionParamsDefinition</a>, ... ]</i>,
        "<a href="#corspolicy" title="CorsPolicy">CorsPolicy</a>" : <i>[ <a href="corspolicydefinition.md">CorsPolicyDefinition</a>, ... ]</i>,
        "<a href="#dynamicreverseproxy" title="DynamicReverseProxy">DynamicReverseProxy</a>" : <i>[ <a href="dynamicreverseproxydefinition.md">DynamicReverseProxyDefinition</a>, ... ]</i>,
        "<a href="#jschallenge" title="JsChallenge">JsChallenge</a>" : <i>[ <a href="jschallengedefinition.md">JsChallengeDefinition</a>, ... ]</i>,
        "<a href="#ratelimiter" title="RateLimiter">RateLimiter</a>" : <i>[ <a href="ratelimiterdefinition.md">RateLimiterDefinition</a>, ... ]</i>,
        "<a href="#ratelimiterallowedprefixes" title="RateLimiterAllowedPrefixes">RateLimiterAllowedPrefixes</a>" : <i>[ <a href="ratelimiterallowedprefixesdefinition.md">RateLimiterAllowedPrefixesDefinition</a>, ... ]</i>,
        "<a href="#requestheaderstoadd" title="RequestHeadersToAdd">RequestHeadersToAdd</a>" : <i>[ <a href="requestheaderstoadddefinition.md">RequestHeadersToAddDefinition</a>, ... ]</i>,
        "<a href="#responseheaderstoadd" title="ResponseHeadersToAdd">ResponseHeadersToAdd</a>" : <i>[ <a href="responseheaderstoadddefinition.md">ResponseHeadersToAddDefinition</a>, ... ]</i>,
        "<a href="#retrypolicy" title="RetryPolicy">RetryPolicy</a>" : <i>[ <a href="retrypolicydefinition.md">RetryPolicyDefinition</a>, ... ]</i>,
        "<a href="#routes" title="Routes">Routes</a>" : <i>[ <a href="routesdefinition.md">RoutesDefinition</a>, ... ]</i>,
        "<a href="#temporaryuserblocking" title="TemporaryUserBlocking">TemporaryUserBlocking</a>" : <i>[ <a href="temporaryuserblockingdefinition.md">TemporaryUserBlockingDefinition</a>, ... ]</i>,
        "<a href="#tlsparameters" title="TlsParameters">TlsParameters</a>" : <i>[ <a href="tlsparametersdefinition.md">TlsParametersDefinition</a>, ... ]</i>,
        "<a href="#useridentification" title="UserIdentification">UserIdentification</a>" : <i>[ <a href="useridentificationdefinition.md">UserIdentificationDefinition</a>, ... ]</i>,
        "<a href="#waftype" title="WafType">WafType</a>" : <i>[ <a href="waftypedefinition.md">WafTypeDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Volterra::VirtualHost
Properties:
    <a href="#addlocation" title="AddLocation">AddLocation</a>: <i>Boolean</i>
    <a href="#annotations" title="Annotations">Annotations</a>: <i>
      - <a href="annotationsdefinition.md">AnnotationsDefinition</a></i>
    <a href="#appendservername" title="AppendServerName">AppendServerName</a>: <i>String</i>
    <a href="#customerrors" title="CustomErrors">CustomErrors</a>: <i>
      - <a href="customerrorsdefinition.md">CustomErrorsDefinition</a></i>
    <a href="#defaultheader" title="DefaultHeader">DefaultHeader</a>: <i>Boolean</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#disable" title="Disable">Disable</a>: <i>Boolean</i>
    <a href="#disabledefaulterrorpages" title="DisableDefaultErrorPages">DisableDefaultErrorPages</a>: <i>Boolean</i>
    <a href="#disablednsresolve" title="DisableDnsResolve">DisableDnsResolve</a>: <i>Boolean</i>
    <a href="#domains" title="Domains">Domains</a>: <i>
      - String</i>
    <a href="#idletimeout" title="IdleTimeout">IdleTimeout</a>: <i>Double</i>
    <a href="#labels" title="Labels">Labels</a>: <i>
      - <a href="labelsdefinition.md">LabelsDefinition</a></i>
    <a href="#maxrequestheadersize" title="MaxRequestHeaderSize">MaxRequestHeaderSize</a>: <i>Double</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#namespace" title="Namespace">Namespace</a>: <i>String</i>
    <a href="#noauthentication" title="NoAuthentication">NoAuthentication</a>: <i>Boolean</i>
    <a href="#nochallenge" title="NoChallenge">NoChallenge</a>: <i>Boolean</i>
    <a href="#passthrough" title="PassThrough">PassThrough</a>: <i>Boolean</i>
    <a href="#proxy" title="Proxy">Proxy</a>: <i>String</i>
    <a href="#requestheaderstoremove" title="RequestHeadersToRemove">RequestHeadersToRemove</a>: <i>
      - String</i>
    <a href="#responseheaderstoremove" title="ResponseHeadersToRemove">ResponseHeadersToRemove</a>: <i>
      - String</i>
    <a href="#servername" title="ServerName">ServerName</a>: <i>String</i>
    <a href="#advertisepolicies" title="AdvertisePolicies">AdvertisePolicies</a>: <i>
      - <a href="advertisepoliciesdefinition.md">AdvertisePoliciesDefinition</a></i>
    <a href="#authentication" title="Authentication">Authentication</a>: <i>
      - <a href="authenticationdefinition.md">AuthenticationDefinition</a></i>
    <a href="#bufferpolicy" title="BufferPolicy">BufferPolicy</a>: <i>
      - <a href="bufferpolicydefinition.md">BufferPolicyDefinition</a></i>
    <a href="#captchachallenge" title="CaptchaChallenge">CaptchaChallenge</a>: <i>
      - <a href="captchachallengedefinition.md">CaptchaChallengeDefinition</a></i>
    <a href="#compressionparams" title="CompressionParams">CompressionParams</a>: <i>
      - <a href="compressionparamsdefinition.md">CompressionParamsDefinition</a></i>
    <a href="#corspolicy" title="CorsPolicy">CorsPolicy</a>: <i>
      - <a href="corspolicydefinition.md">CorsPolicyDefinition</a></i>
    <a href="#dynamicreverseproxy" title="DynamicReverseProxy">DynamicReverseProxy</a>: <i>
      - <a href="dynamicreverseproxydefinition.md">DynamicReverseProxyDefinition</a></i>
    <a href="#jschallenge" title="JsChallenge">JsChallenge</a>: <i>
      - <a href="jschallengedefinition.md">JsChallengeDefinition</a></i>
    <a href="#ratelimiter" title="RateLimiter">RateLimiter</a>: <i>
      - <a href="ratelimiterdefinition.md">RateLimiterDefinition</a></i>
    <a href="#ratelimiterallowedprefixes" title="RateLimiterAllowedPrefixes">RateLimiterAllowedPrefixes</a>: <i>
      - <a href="ratelimiterallowedprefixesdefinition.md">RateLimiterAllowedPrefixesDefinition</a></i>
    <a href="#requestheaderstoadd" title="RequestHeadersToAdd">RequestHeadersToAdd</a>: <i>
      - <a href="requestheaderstoadddefinition.md">RequestHeadersToAddDefinition</a></i>
    <a href="#responseheaderstoadd" title="ResponseHeadersToAdd">ResponseHeadersToAdd</a>: <i>
      - <a href="responseheaderstoadddefinition.md">ResponseHeadersToAddDefinition</a></i>
    <a href="#retrypolicy" title="RetryPolicy">RetryPolicy</a>: <i>
      - <a href="retrypolicydefinition.md">RetryPolicyDefinition</a></i>
    <a href="#routes" title="Routes">Routes</a>: <i>
      - <a href="routesdefinition.md">RoutesDefinition</a></i>
    <a href="#temporaryuserblocking" title="TemporaryUserBlocking">TemporaryUserBlocking</a>: <i>
      - <a href="temporaryuserblockingdefinition.md">TemporaryUserBlockingDefinition</a></i>
    <a href="#tlsparameters" title="TlsParameters">TlsParameters</a>: <i>
      - <a href="tlsparametersdefinition.md">TlsParametersDefinition</a></i>
    <a href="#useridentification" title="UserIdentification">UserIdentification</a>: <i>
      - <a href="useridentificationdefinition.md">UserIdentificationDefinition</a></i>
    <a href="#waftype" title="WafType">WafType</a>: <i>
      - <a href="waftypedefinition.md">WafTypeDefinition</a></i>
</pre>

## Properties

#### AddLocation

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Annotations

_Required_: No

_Type_: List of <a href="annotationsdefinition.md">AnnotationsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AppendServerName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CustomErrors

_Required_: No

_Type_: List of <a href="customerrorsdefinition.md">CustomErrorsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefaultHeader

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Disable

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisableDefaultErrorPages

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisableDnsResolve

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Domains

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IdleTimeout

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Labels

_Required_: No

_Type_: List of <a href="labelsdefinition.md">LabelsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxRequestHeaderSize

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Namespace

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NoAuthentication

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NoChallenge

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PassThrough

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Proxy

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RequestHeadersToRemove

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResponseHeadersToRemove

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServerName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AdvertisePolicies

_Required_: No

_Type_: List of <a href="advertisepoliciesdefinition.md">AdvertisePoliciesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Authentication

_Required_: No

_Type_: List of <a href="authenticationdefinition.md">AuthenticationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BufferPolicy

_Required_: No

_Type_: List of <a href="bufferpolicydefinition.md">BufferPolicyDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CaptchaChallenge

_Required_: No

_Type_: List of <a href="captchachallengedefinition.md">CaptchaChallengeDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CompressionParams

_Required_: No

_Type_: List of <a href="compressionparamsdefinition.md">CompressionParamsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CorsPolicy

_Required_: No

_Type_: List of <a href="corspolicydefinition.md">CorsPolicyDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DynamicReverseProxy

_Required_: No

_Type_: List of <a href="dynamicreverseproxydefinition.md">DynamicReverseProxyDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### JsChallenge

_Required_: No

_Type_: List of <a href="jschallengedefinition.md">JsChallengeDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RateLimiter

_Required_: No

_Type_: List of <a href="ratelimiterdefinition.md">RateLimiterDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RateLimiterAllowedPrefixes

_Required_: No

_Type_: List of <a href="ratelimiterallowedprefixesdefinition.md">RateLimiterAllowedPrefixesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RequestHeadersToAdd

_Required_: No

_Type_: List of <a href="requestheaderstoadddefinition.md">RequestHeadersToAddDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResponseHeadersToAdd

_Required_: No

_Type_: List of <a href="responseheaderstoadddefinition.md">ResponseHeadersToAddDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RetryPolicy

_Required_: No

_Type_: List of <a href="retrypolicydefinition.md">RetryPolicyDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Routes

_Required_: No

_Type_: List of <a href="routesdefinition.md">RoutesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TemporaryUserBlocking

_Required_: No

_Type_: List of <a href="temporaryuserblockingdefinition.md">TemporaryUserBlockingDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TlsParameters

_Required_: No

_Type_: List of <a href="tlsparametersdefinition.md">TlsParametersDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UserIdentification

_Required_: No

_Type_: List of <a href="useridentificationdefinition.md">UserIdentificationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WafType

_Required_: No

_Type_: List of <a href="waftypedefinition.md">WafTypeDefinition</a>

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

