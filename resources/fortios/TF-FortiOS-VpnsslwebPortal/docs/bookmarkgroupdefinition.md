# TF::FortiOS::VpnsslwebPortal BookmarkGroupDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#bookmarks" title="Bookmarks">Bookmarks</a>" : <i>[ <a href="bookmarksdefinition.md">BookmarksDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#bookmarks" title="Bookmarks">Bookmarks</a>: <i>
      - <a href="bookmarksdefinition.md">BookmarksDefinition</a></i>
</pre>

## Properties

#### Name

Bookmark group name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Bookmarks

_Required_: No

_Type_: List of <a href="bookmarksdefinition.md">BookmarksDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

