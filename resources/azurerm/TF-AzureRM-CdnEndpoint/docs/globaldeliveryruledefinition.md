# TF::AzureRM::CdnEndpoint GlobalDeliveryRuleDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#cacheexpirationaction" title="CacheExpirationAction">CacheExpirationAction</a>" : <i>[ <a href="cacheexpirationactiondefinition.md">CacheExpirationActionDefinition</a>, ... ]</i>,
    "<a href="#cachekeyquerystringaction" title="CacheKeyQueryStringAction">CacheKeyQueryStringAction</a>" : <i>[ <a href="cachekeyquerystringactiondefinition.md">CacheKeyQueryStringActionDefinition</a>, ... ]</i>,
    "<a href="#modifyrequestheaderaction" title="ModifyRequestHeaderAction">ModifyRequestHeaderAction</a>" : <i>[ <a href="modifyrequestheaderactiondefinition.md">ModifyRequestHeaderActionDefinition</a>, ... ]</i>,
    "<a href="#modifyresponseheaderaction" title="ModifyResponseHeaderAction">ModifyResponseHeaderAction</a>" : <i>[ <a href="modifyresponseheaderactiondefinition.md">ModifyResponseHeaderActionDefinition</a>, ... ]</i>,
    "<a href="#urlredirectaction" title="UrlRedirectAction">UrlRedirectAction</a>" : <i>[ <a href="urlredirectactiondefinition.md">UrlRedirectActionDefinition</a>, ... ]</i>,
    "<a href="#urlrewriteaction" title="UrlRewriteAction">UrlRewriteAction</a>" : <i>[ <a href="urlrewriteactiondefinition.md">UrlRewriteActionDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#cacheexpirationaction" title="CacheExpirationAction">CacheExpirationAction</a>: <i>
      - <a href="cacheexpirationactiondefinition.md">CacheExpirationActionDefinition</a></i>
<a href="#cachekeyquerystringaction" title="CacheKeyQueryStringAction">CacheKeyQueryStringAction</a>: <i>
      - <a href="cachekeyquerystringactiondefinition.md">CacheKeyQueryStringActionDefinition</a></i>
<a href="#modifyrequestheaderaction" title="ModifyRequestHeaderAction">ModifyRequestHeaderAction</a>: <i>
      - <a href="modifyrequestheaderactiondefinition.md">ModifyRequestHeaderActionDefinition</a></i>
<a href="#modifyresponseheaderaction" title="ModifyResponseHeaderAction">ModifyResponseHeaderAction</a>: <i>
      - <a href="modifyresponseheaderactiondefinition.md">ModifyResponseHeaderActionDefinition</a></i>
<a href="#urlredirectaction" title="UrlRedirectAction">UrlRedirectAction</a>: <i>
      - <a href="urlredirectactiondefinition.md">UrlRedirectActionDefinition</a></i>
<a href="#urlrewriteaction" title="UrlRewriteAction">UrlRewriteAction</a>: <i>
      - <a href="urlrewriteactiondefinition.md">UrlRewriteActionDefinition</a></i>
</pre>

## Properties

#### CacheExpirationAction

_Required_: No

_Type_: List of <a href="cacheexpirationactiondefinition.md">CacheExpirationActionDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CacheKeyQueryStringAction

_Required_: No

_Type_: List of <a href="cachekeyquerystringactiondefinition.md">CacheKeyQueryStringActionDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ModifyRequestHeaderAction

_Required_: No

_Type_: List of <a href="modifyrequestheaderactiondefinition.md">ModifyRequestHeaderActionDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ModifyResponseHeaderAction

_Required_: No

_Type_: List of <a href="modifyresponseheaderactiondefinition.md">ModifyResponseHeaderActionDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UrlRedirectAction

_Required_: No

_Type_: List of <a href="urlredirectactiondefinition.md">UrlRedirectActionDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UrlRewriteAction

_Required_: No

_Type_: List of <a href="urlrewriteactiondefinition.md">UrlRewriteActionDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

