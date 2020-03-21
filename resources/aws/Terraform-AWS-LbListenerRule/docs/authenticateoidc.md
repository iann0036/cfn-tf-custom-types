# Terraform::AWS::LbListenerRule AuthenticateOidc

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#authenticationrequestextraparams" title="AuthenticationRequestExtraParams">AuthenticationRequestExtraParams</a>" : <i>[ &lt;a href=&#34;authenticateoidc-authenticationrequestextraparams.md&#34;&gt;AuthenticationRequestExtraParams&lt;/a&gt;, ... ]</i>,
    "<a href="#authorizationendpoint" title="AuthorizationEndpoint">AuthorizationEndpoint</a>" : <i>String</i>,
    "<a href="#clientid" title="ClientId">ClientId</a>" : <i>String</i>,
    "<a href="#clientsecret" title="ClientSecret">ClientSecret</a>" : <i>String</i>,
    "<a href="#issuer" title="Issuer">Issuer</a>" : <i>String</i>,
    "<a href="#onunauthenticatedrequest" title="OnUnauthenticatedRequest">OnUnauthenticatedRequest</a>" : <i>String</i>,
    "<a href="#scope" title="Scope">Scope</a>" : <i>String</i>,
    "<a href="#sessioncookiename" title="SessionCookieName">SessionCookieName</a>" : <i>String</i>,
    "<a href="#sessiontimeout" title="SessionTimeout">SessionTimeout</a>" : <i>Double</i>,
    "<a href="#tokenendpoint" title="TokenEndpoint">TokenEndpoint</a>" : <i>String</i>,
    "<a href="#userinfoendpoint" title="UserInfoEndpoint">UserInfoEndpoint</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#authenticationrequestextraparams" title="AuthenticationRequestExtraParams">AuthenticationRequestExtraParams</a>: <i>
      - &lt;a href=&#34;authenticateoidc-authenticationrequestextraparams.md&#34;&gt;AuthenticationRequestExtraParams&lt;/a&gt;</i>
<a href="#authorizationendpoint" title="AuthorizationEndpoint">AuthorizationEndpoint</a>: <i>String</i>
<a href="#clientid" title="ClientId">ClientId</a>: <i>String</i>
<a href="#clientsecret" title="ClientSecret">ClientSecret</a>: <i>String</i>
<a href="#issuer" title="Issuer">Issuer</a>: <i>String</i>
<a href="#onunauthenticatedrequest" title="OnUnauthenticatedRequest">OnUnauthenticatedRequest</a>: <i>String</i>
<a href="#scope" title="Scope">Scope</a>: <i>String</i>
<a href="#sessioncookiename" title="SessionCookieName">SessionCookieName</a>: <i>String</i>
<a href="#sessiontimeout" title="SessionTimeout">SessionTimeout</a>: <i>Double</i>
<a href="#tokenendpoint" title="TokenEndpoint">TokenEndpoint</a>: <i>String</i>
<a href="#userinfoendpoint" title="UserInfoEndpoint">UserInfoEndpoint</a>: <i>String</i>
</pre>

## Properties

#### AuthenticationRequestExtraParams

_Required_: No
_Type_: List of &lt;a href=&#34;authenticateoidc-authenticationrequestextraparams.md&#34;&gt;AuthenticationRequestExtraParams&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AuthorizationEndpoint

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClientId

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClientSecret

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Issuer

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OnUnauthenticatedRequest

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Scope

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SessionCookieName

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SessionTimeout

_Required_: No
_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TokenEndpoint

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UserInfoEndpoint

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

