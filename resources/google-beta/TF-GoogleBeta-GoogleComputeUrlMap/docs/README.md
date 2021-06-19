# TF::GoogleBeta::GoogleComputeUrlMap

CloudFormation equivalent of google_compute_url_map

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::GoogleBeta::GoogleComputeUrlMap",
    "Properties" : {
        "<a href="#defaultservice" title="DefaultService">DefaultService</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#project" title="Project">Project</a>" : <i>String</i>,
        "<a href="#defaultrouteaction" title="DefaultRouteAction">DefaultRouteAction</a>" : <i>[ <a href="defaultrouteactiondefinition.md">DefaultRouteActionDefinition</a>, ... ]</i>,
        "<a href="#defaulturlredirect" title="DefaultUrlRedirect">DefaultUrlRedirect</a>" : <i>[ <a href="defaulturlredirectdefinition.md">DefaultUrlRedirectDefinition</a>, ... ]</i>,
        "<a href="#headeraction" title="HeaderAction">HeaderAction</a>" : <i>[ <a href="headeractiondefinition.md">HeaderActionDefinition</a>, ... ]</i>,
        "<a href="#hostrule" title="HostRule">HostRule</a>" : <i>[ <a href="hostruledefinition.md">HostRuleDefinition</a>, ... ]</i>,
        "<a href="#pathmatcher" title="PathMatcher">PathMatcher</a>" : <i>[ <a href="pathmatcherdefinition.md">PathMatcherDefinition</a>, ... ]</i>,
        "<a href="#test" title="Test">Test</a>" : <i>[ <a href="testdefinition.md">TestDefinition</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::GoogleBeta::GoogleComputeUrlMap
Properties:
    <a href="#defaultservice" title="DefaultService">DefaultService</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#project" title="Project">Project</a>: <i>String</i>
    <a href="#defaultrouteaction" title="DefaultRouteAction">DefaultRouteAction</a>: <i>
      - <a href="defaultrouteactiondefinition.md">DefaultRouteActionDefinition</a></i>
    <a href="#defaulturlredirect" title="DefaultUrlRedirect">DefaultUrlRedirect</a>: <i>
      - <a href="defaulturlredirectdefinition.md">DefaultUrlRedirectDefinition</a></i>
    <a href="#headeraction" title="HeaderAction">HeaderAction</a>: <i>
      - <a href="headeractiondefinition.md">HeaderActionDefinition</a></i>
    <a href="#hostrule" title="HostRule">HostRule</a>: <i>
      - <a href="hostruledefinition.md">HostRuleDefinition</a></i>
    <a href="#pathmatcher" title="PathMatcher">PathMatcher</a>: <i>
      - <a href="pathmatcherdefinition.md">PathMatcherDefinition</a></i>
    <a href="#test" title="Test">Test</a>: <i>
      - <a href="testdefinition.md">TestDefinition</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### DefaultService

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Project

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefaultRouteAction

_Required_: No

_Type_: List of <a href="defaultrouteactiondefinition.md">DefaultRouteActionDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefaultUrlRedirect

_Required_: No

_Type_: List of <a href="defaulturlredirectdefinition.md">DefaultUrlRedirectDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HeaderAction

_Required_: No

_Type_: List of <a href="headeractiondefinition.md">HeaderActionDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HostRule

_Required_: No

_Type_: List of <a href="hostruledefinition.md">HostRuleDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PathMatcher

_Required_: No

_Type_: List of <a href="pathmatcherdefinition.md">PathMatcherDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Test

_Required_: No

_Type_: List of <a href="testdefinition.md">TestDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeoutsdefinition.md">TimeoutsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### CreationTimestamp

Returns the <code>CreationTimestamp</code> value.

#### Fingerprint

Returns the <code>Fingerprint</code> value.

#### Id

Returns the <code>Id</code> value.

#### MapId

Returns the <code>MapId</code> value.

#### SelfLink

Returns the <code>SelfLink</code> value.

