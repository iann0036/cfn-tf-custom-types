# TF::AVI::Applicationprofile CacheConfigDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#ageheader" title="AgeHeader">AgeHeader</a>" : <i>Boolean</i>,
    "<a href="#aggressive" title="Aggressive">Aggressive</a>" : <i>Boolean</i>,
    "<a href="#dateheader" title="DateHeader">DateHeader</a>" : <i>Boolean</i>,
    "<a href="#defaultexpire" title="DefaultExpire">DefaultExpire</a>" : <i>Double</i>,
    "<a href="#enabled" title="Enabled">Enabled</a>" : <i>Boolean</i>,
    "<a href="#heuristicexpire" title="HeuristicExpire">HeuristicExpire</a>" : <i>Boolean</i>,
    "<a href="#ignorerequestcachecontrol" title="IgnoreRequestCacheControl">IgnoreRequestCacheControl</a>" : <i>Boolean</i>,
    "<a href="#maxcachesize" title="MaxCacheSize">MaxCacheSize</a>" : <i>Double</i>,
    "<a href="#maxobjectsize" title="MaxObjectSize">MaxObjectSize</a>" : <i>Double</i>,
    "<a href="#mimetypesblockgrouprefs" title="MimeTypesBlockGroupRefs">MimeTypesBlockGroupRefs</a>" : <i>[ String, ... ]</i>,
    "<a href="#mimetypesblocklists" title="MimeTypesBlockLists">MimeTypesBlockLists</a>" : <i>[ String, ... ]</i>,
    "<a href="#mimetypesgrouprefs" title="MimeTypesGroupRefs">MimeTypesGroupRefs</a>" : <i>[ String, ... ]</i>,
    "<a href="#mimetypeslist" title="MimeTypesList">MimeTypesList</a>" : <i>[ String, ... ]</i>,
    "<a href="#minobjectsize" title="MinObjectSize">MinObjectSize</a>" : <i>Double</i>,
    "<a href="#querycacheable" title="QueryCacheable">QueryCacheable</a>" : <i>Boolean</i>,
    "<a href="#xcacheheader" title="XcacheHeader">XcacheHeader</a>" : <i>Boolean</i>,
    "<a href="#urinoncacheable" title="UriNonCacheable">UriNonCacheable</a>" : <i>[ <a href="urinoncacheabledefinition.md">UriNonCacheableDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#ageheader" title="AgeHeader">AgeHeader</a>: <i>Boolean</i>
<a href="#aggressive" title="Aggressive">Aggressive</a>: <i>Boolean</i>
<a href="#dateheader" title="DateHeader">DateHeader</a>: <i>Boolean</i>
<a href="#defaultexpire" title="DefaultExpire">DefaultExpire</a>: <i>Double</i>
<a href="#enabled" title="Enabled">Enabled</a>: <i>Boolean</i>
<a href="#heuristicexpire" title="HeuristicExpire">HeuristicExpire</a>: <i>Boolean</i>
<a href="#ignorerequestcachecontrol" title="IgnoreRequestCacheControl">IgnoreRequestCacheControl</a>: <i>Boolean</i>
<a href="#maxcachesize" title="MaxCacheSize">MaxCacheSize</a>: <i>Double</i>
<a href="#maxobjectsize" title="MaxObjectSize">MaxObjectSize</a>: <i>Double</i>
<a href="#mimetypesblockgrouprefs" title="MimeTypesBlockGroupRefs">MimeTypesBlockGroupRefs</a>: <i>
      - String</i>
<a href="#mimetypesblocklists" title="MimeTypesBlockLists">MimeTypesBlockLists</a>: <i>
      - String</i>
<a href="#mimetypesgrouprefs" title="MimeTypesGroupRefs">MimeTypesGroupRefs</a>: <i>
      - String</i>
<a href="#mimetypeslist" title="MimeTypesList">MimeTypesList</a>: <i>
      - String</i>
<a href="#minobjectsize" title="MinObjectSize">MinObjectSize</a>: <i>Double</i>
<a href="#querycacheable" title="QueryCacheable">QueryCacheable</a>: <i>Boolean</i>
<a href="#xcacheheader" title="XcacheHeader">XcacheHeader</a>: <i>Boolean</i>
<a href="#urinoncacheable" title="UriNonCacheable">UriNonCacheable</a>: <i>
      - <a href="urinoncacheabledefinition.md">UriNonCacheableDefinition</a></i>
</pre>

## Properties

#### AgeHeader

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Aggressive

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DateHeader

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefaultExpire

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Enabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HeuristicExpire

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IgnoreRequestCacheControl

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxCacheSize

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxObjectSize

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MimeTypesBlockGroupRefs

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MimeTypesBlockLists

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MimeTypesGroupRefs

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MimeTypesList

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MinObjectSize

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### QueryCacheable

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### XcacheHeader

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UriNonCacheable

_Required_: No

_Type_: List of <a href="urinoncacheabledefinition.md">UriNonCacheableDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

