# TF::AzureRM::CdnEndpoint DeliveryRuleDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#order" title="Order">Order</a>" : <i>Double</i>,
    "<a href="#cacheexpirationaction" title="CacheExpirationAction">CacheExpirationAction</a>" : <i>[ <a href="cacheexpirationactiondefinition.md">CacheExpirationActionDefinition</a>, ... ]</i>,
    "<a href="#cachekeyquerystringaction" title="CacheKeyQueryStringAction">CacheKeyQueryStringAction</a>" : <i>[ <a href="cachekeyquerystringactiondefinition.md">CacheKeyQueryStringActionDefinition</a>, ... ]</i>,
    "<a href="#cookiescondition" title="CookiesCondition">CookiesCondition</a>" : <i>[ <a href="cookiesconditiondefinition.md">CookiesConditionDefinition</a>, ... ]</i>,
    "<a href="#devicecondition" title="DeviceCondition">DeviceCondition</a>" : <i>[ <a href="deviceconditiondefinition.md">DeviceConditionDefinition</a>, ... ]</i>,
    "<a href="#httpversioncondition" title="HttpVersionCondition">HttpVersionCondition</a>" : <i>[ <a href="httpversionconditiondefinition.md">HttpVersionConditionDefinition</a>, ... ]</i>,
    "<a href="#modifyrequestheaderaction" title="ModifyRequestHeaderAction">ModifyRequestHeaderAction</a>" : <i>[ <a href="modifyrequestheaderactiondefinition.md">ModifyRequestHeaderActionDefinition</a>, ... ]</i>,
    "<a href="#modifyresponseheaderaction" title="ModifyResponseHeaderAction">ModifyResponseHeaderAction</a>" : <i>[ <a href="modifyresponseheaderactiondefinition.md">ModifyResponseHeaderActionDefinition</a>, ... ]</i>,
    "<a href="#postargcondition" title="PostArgCondition">PostArgCondition</a>" : <i>[ <a href="postargconditiondefinition.md">PostArgConditionDefinition</a>, ... ]</i>,
    "<a href="#querystringcondition" title="QueryStringCondition">QueryStringCondition</a>" : <i>[ <a href="querystringconditiondefinition.md">QueryStringConditionDefinition</a>, ... ]</i>,
    "<a href="#remoteaddresscondition" title="RemoteAddressCondition">RemoteAddressCondition</a>" : <i>[ <a href="remoteaddressconditiondefinition.md">RemoteAddressConditionDefinition</a>, ... ]</i>,
    "<a href="#requestbodycondition" title="RequestBodyCondition">RequestBodyCondition</a>" : <i>[ <a href="requestbodyconditiondefinition.md">RequestBodyConditionDefinition</a>, ... ]</i>,
    "<a href="#requestheadercondition" title="RequestHeaderCondition">RequestHeaderCondition</a>" : <i>[ <a href="requestheaderconditiondefinition.md">RequestHeaderConditionDefinition</a>, ... ]</i>,
    "<a href="#requestmethodcondition" title="RequestMethodCondition">RequestMethodCondition</a>" : <i>[ <a href="requestmethodconditiondefinition.md">RequestMethodConditionDefinition</a>, ... ]</i>,
    "<a href="#requestschemecondition" title="RequestSchemeCondition">RequestSchemeCondition</a>" : <i>[ <a href="requestschemeconditiondefinition.md">RequestSchemeConditionDefinition</a>, ... ]</i>,
    "<a href="#requesturicondition" title="RequestUriCondition">RequestUriCondition</a>" : <i>[ <a href="requesturiconditiondefinition.md">RequestUriConditionDefinition</a>, ... ]</i>,
    "<a href="#urlfileextensioncondition" title="UrlFileExtensionCondition">UrlFileExtensionCondition</a>" : <i>[ <a href="urlfileextensionconditiondefinition.md">UrlFileExtensionConditionDefinition</a>, ... ]</i>,
    "<a href="#urlfilenamecondition" title="UrlFileNameCondition">UrlFileNameCondition</a>" : <i>[ <a href="urlfilenameconditiondefinition.md">UrlFileNameConditionDefinition</a>, ... ]</i>,
    "<a href="#urlpathcondition" title="UrlPathCondition">UrlPathCondition</a>" : <i>[ <a href="urlpathconditiondefinition.md">UrlPathConditionDefinition</a>, ... ]</i>,
    "<a href="#urlredirectaction" title="UrlRedirectAction">UrlRedirectAction</a>" : <i>[ <a href="urlredirectactiondefinition.md">UrlRedirectActionDefinition</a>, ... ]</i>,
    "<a href="#urlrewriteaction" title="UrlRewriteAction">UrlRewriteAction</a>" : <i>[ <a href="urlrewriteactiondefinition.md">UrlRewriteActionDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#order" title="Order">Order</a>: <i>Double</i>
<a href="#cacheexpirationaction" title="CacheExpirationAction">CacheExpirationAction</a>: <i>
      - <a href="cacheexpirationactiondefinition.md">CacheExpirationActionDefinition</a></i>
<a href="#cachekeyquerystringaction" title="CacheKeyQueryStringAction">CacheKeyQueryStringAction</a>: <i>
      - <a href="cachekeyquerystringactiondefinition.md">CacheKeyQueryStringActionDefinition</a></i>
<a href="#cookiescondition" title="CookiesCondition">CookiesCondition</a>: <i>
      - <a href="cookiesconditiondefinition.md">CookiesConditionDefinition</a></i>
<a href="#devicecondition" title="DeviceCondition">DeviceCondition</a>: <i>
      - <a href="deviceconditiondefinition.md">DeviceConditionDefinition</a></i>
<a href="#httpversioncondition" title="HttpVersionCondition">HttpVersionCondition</a>: <i>
      - <a href="httpversionconditiondefinition.md">HttpVersionConditionDefinition</a></i>
<a href="#modifyrequestheaderaction" title="ModifyRequestHeaderAction">ModifyRequestHeaderAction</a>: <i>
      - <a href="modifyrequestheaderactiondefinition.md">ModifyRequestHeaderActionDefinition</a></i>
<a href="#modifyresponseheaderaction" title="ModifyResponseHeaderAction">ModifyResponseHeaderAction</a>: <i>
      - <a href="modifyresponseheaderactiondefinition.md">ModifyResponseHeaderActionDefinition</a></i>
<a href="#postargcondition" title="PostArgCondition">PostArgCondition</a>: <i>
      - <a href="postargconditiondefinition.md">PostArgConditionDefinition</a></i>
<a href="#querystringcondition" title="QueryStringCondition">QueryStringCondition</a>: <i>
      - <a href="querystringconditiondefinition.md">QueryStringConditionDefinition</a></i>
<a href="#remoteaddresscondition" title="RemoteAddressCondition">RemoteAddressCondition</a>: <i>
      - <a href="remoteaddressconditiondefinition.md">RemoteAddressConditionDefinition</a></i>
<a href="#requestbodycondition" title="RequestBodyCondition">RequestBodyCondition</a>: <i>
      - <a href="requestbodyconditiondefinition.md">RequestBodyConditionDefinition</a></i>
<a href="#requestheadercondition" title="RequestHeaderCondition">RequestHeaderCondition</a>: <i>
      - <a href="requestheaderconditiondefinition.md">RequestHeaderConditionDefinition</a></i>
<a href="#requestmethodcondition" title="RequestMethodCondition">RequestMethodCondition</a>: <i>
      - <a href="requestmethodconditiondefinition.md">RequestMethodConditionDefinition</a></i>
<a href="#requestschemecondition" title="RequestSchemeCondition">RequestSchemeCondition</a>: <i>
      - <a href="requestschemeconditiondefinition.md">RequestSchemeConditionDefinition</a></i>
<a href="#requesturicondition" title="RequestUriCondition">RequestUriCondition</a>: <i>
      - <a href="requesturiconditiondefinition.md">RequestUriConditionDefinition</a></i>
<a href="#urlfileextensioncondition" title="UrlFileExtensionCondition">UrlFileExtensionCondition</a>: <i>
      - <a href="urlfileextensionconditiondefinition.md">UrlFileExtensionConditionDefinition</a></i>
<a href="#urlfilenamecondition" title="UrlFileNameCondition">UrlFileNameCondition</a>: <i>
      - <a href="urlfilenameconditiondefinition.md">UrlFileNameConditionDefinition</a></i>
<a href="#urlpathcondition" title="UrlPathCondition">UrlPathCondition</a>: <i>
      - <a href="urlpathconditiondefinition.md">UrlPathConditionDefinition</a></i>
<a href="#urlredirectaction" title="UrlRedirectAction">UrlRedirectAction</a>: <i>
      - <a href="urlredirectactiondefinition.md">UrlRedirectActionDefinition</a></i>
<a href="#urlrewriteaction" title="UrlRewriteAction">UrlRewriteAction</a>: <i>
      - <a href="urlrewriteactiondefinition.md">UrlRewriteActionDefinition</a></i>
</pre>

## Properties

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Order

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CacheExpirationAction

_Required_: No

_Type_: List of <a href="cacheexpirationactiondefinition.md">CacheExpirationActionDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CacheKeyQueryStringAction

_Required_: No

_Type_: List of <a href="cachekeyquerystringactiondefinition.md">CacheKeyQueryStringActionDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CookiesCondition

_Required_: No

_Type_: List of <a href="cookiesconditiondefinition.md">CookiesConditionDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DeviceCondition

_Required_: No

_Type_: List of <a href="deviceconditiondefinition.md">DeviceConditionDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HttpVersionCondition

_Required_: No

_Type_: List of <a href="httpversionconditiondefinition.md">HttpVersionConditionDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ModifyRequestHeaderAction

_Required_: No

_Type_: List of <a href="modifyrequestheaderactiondefinition.md">ModifyRequestHeaderActionDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ModifyResponseHeaderAction

_Required_: No

_Type_: List of <a href="modifyresponseheaderactiondefinition.md">ModifyResponseHeaderActionDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PostArgCondition

_Required_: No

_Type_: List of <a href="postargconditiondefinition.md">PostArgConditionDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### QueryStringCondition

_Required_: No

_Type_: List of <a href="querystringconditiondefinition.md">QueryStringConditionDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RemoteAddressCondition

_Required_: No

_Type_: List of <a href="remoteaddressconditiondefinition.md">RemoteAddressConditionDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RequestBodyCondition

_Required_: No

_Type_: List of <a href="requestbodyconditiondefinition.md">RequestBodyConditionDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RequestHeaderCondition

_Required_: No

_Type_: List of <a href="requestheaderconditiondefinition.md">RequestHeaderConditionDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RequestMethodCondition

_Required_: No

_Type_: List of <a href="requestmethodconditiondefinition.md">RequestMethodConditionDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RequestSchemeCondition

_Required_: No

_Type_: List of <a href="requestschemeconditiondefinition.md">RequestSchemeConditionDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RequestUriCondition

_Required_: No

_Type_: List of <a href="requesturiconditiondefinition.md">RequestUriConditionDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UrlFileExtensionCondition

_Required_: No

_Type_: List of <a href="urlfileextensionconditiondefinition.md">UrlFileExtensionConditionDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UrlFileNameCondition

_Required_: No

_Type_: List of <a href="urlfilenameconditiondefinition.md">UrlFileNameConditionDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UrlPathCondition

_Required_: No

_Type_: List of <a href="urlpathconditiondefinition.md">UrlPathConditionDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UrlRedirectAction

_Required_: No

_Type_: List of <a href="urlredirectactiondefinition.md">UrlRedirectActionDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UrlRewriteAction

_Required_: No

_Type_: List of <a href="urlrewriteactiondefinition.md">UrlRewriteActionDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

